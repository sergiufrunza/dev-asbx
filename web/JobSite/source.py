import csv
from slugify import slugify

from .models import *
from Location.models import City, State, ZipCode




def upload_boiler():
    file = open("JobSite/upload/FloridaFinish.csv", "r")
    list_row = list(csv.reader(file))
    for row in list_row:
        if row[0] != "Location":
            location = row[0]
            address = row[1]
            manufacturer = row[5]
            year_built = row[6]
            city = City.objects.filter(search_slug=slugify(row[2] +" "+row[3]))
            state = State.objects.get(abbr=row[3])
            zip = ZipCode.objects.filter(code = str(row[4]))
            if city.exists() and zip.exists():
                print(row[2], row[3], row[4])
                Boiler.objects.create(
                    location=location,
                    address=address,
                    state=state,
                    manufacturer=manufacturer,
                    year_built=year_built,
                    city = city[0],
                    zip = zip[0],
                )





def upload_job_site():
    file = open("JobSite/upload/FloridaJobSite.tsv", "r")
    list_row = list(csv.reader(file, delimiter="\t"))
    for row in list_row:
        name = row[1]
        city = City.objects.filter(search_slug = slugify(row[2]+" "+row[3]))[0]
        state = State.objects.filter(abbr = row[3])[0]
        trust = Trust.objects.get(company_name = row[0])
        if JobSite.objects.filter(slug = slugify(name+" "+city.slug)).exists():
            job_site = JobSite.objects.get(slug = slugify(name+" "+city.slug))
            new_exposure = ExposureHistory.objects.create(
                trust=trust,
                year_from = row[4],
                year_to = row[5]
            )
            job_site.exposure.add(new_exposure)
        else:
            job_site = JobSite.objects.create(
                name = name,
                city=city,
                state=state,
            )
            new_exposure = ExposureHistory.objects.create(
                trust=trust,
                year_from = row[4],
                year_to = row[5]
            )
            job_site.exposure.add(new_exposure)


def calculateCompensation(trusts, diagnostic, smoker, type):
    compensation = 0
    field = ""
    if type == "avg":
        field = 'compensation_avg'
    if type == "ir":
        field = 'compensation_ir'
    if type == "er":
        field = 'compensation_er'

    if diagnostic.name.lower() == "mesothelioma":
        for trust in trusts:
            compensation += int(getattr(trust.mesothelioma, field) * trust.mesothelioma.ratio / 100)

    if diagnostic.name.lower() == "lung cancer":
        for trust in trusts:
            compensation += int(getattr(trust.lung_cancer, field) * trust.lung_cancer.ratio / 100)
        if smoker == "yes":
            compensation -= int((compensation * 15) / 100)

    if diagnostic.name.lower() == "other cancer":
        for trust in trusts:
            compensation += int(getattr(trust.other_cancer, field) * trust.other_cancer.ratio / 100)

    if diagnostic.name.lower() == "severe asbestosis":
        for trust in trusts:
            compensation += int(getattr(trust.severe_asbestosis, field) * trust.severe_asbestosis.ratio / 100)

    if diagnostic.name.lower() == "asbestosis":
        for trust in trusts:
            compensation += int(getattr(trust.asbestosis, field) * trust.asbestosis.ratio / 100)

    return compensation




def upload_disease():
    list_disease = ["Mesothelioma", "Lung Cancer", "Other Cancer", "Severe Asbestosis", "Asbestosis"]
    for disease in list_disease:
        Disease.objects.update_or_create(name=disease)


def upload_trusts():
    file = open("JobSite/upload/asbestos-calculator-data.csv", "r")
    list_trusts = list(csv.reader(file))
    file.close()
    for index, trust in enumerate(list_trusts):
        if index == 0 or not trust[2] or not trust[12] or not trust[6] or trust[12]=="Missing":
            pass
        else:
            print(trust[2])
            states = trust[6].split("\n")
            relation_state = State.objects.filter(abbr__in = states)
            Budget.objects.update_or_create(
                    name=trust[12],
                    initial_amount=trust[10],
                    available_amount=trust[11]
            )
            budget_relation = Budget.objects.get(name=trust[12])

            CompensationAsbestosis.objects.update_or_create(
                name=trust[2],
                compensation_avg=trust[31],
                compensation_er=trust[30],
                compensation_ir=trust[32],
                ratio=float(trust[33].replace("%",""))
            )
            asbestosis = CompensationAsbestosis.objects.get(name=trust[2])
            CompensationSevereAsbestosis.objects.update_or_create(
                name=trust[2],
                compensation_avg=trust[27],
                compensation_er=trust[26],
                compensation_ir=trust[28],
                ratio=float(trust[29].replace("%",""))
            )
            severe_asbestosis = CompensationSevereAsbestosis.objects.get(name=trust[2])
            CompensationMesothelioma.objects.update_or_create(
                name=trust[2],
                compensation_avg=trust[15],
                compensation_er=trust[14],
                compensation_ir=trust[16],
                ratio=float(trust[17].replace("%",""))
            )
            mesothelioma = CompensationMesothelioma.objects.get(name=trust[2])
            CompensationLungCancer.objects.update_or_create(
                name=trust[2],
                compensation_avg=trust[19],
                compensation_er=trust[18],
                compensation_ir=trust[20],
                ratio=float(trust[21].replace("%",""))
            )
            lung_cancer = CompensationLungCancer.objects.get(name=trust[2])

            CompensationOtherCancer.objects.update_or_create(
                name=trust[2],
                compensation_avg=trust[23],
                compensation_er=trust[22],
                compensation_ir=trust[24],
                ratio=float(trust[25].replace("%",""))
            )
            other_cancer = CompensationOtherCancer.objects.get(name=trust[2])
            Trust.objects.update_or_create(
                slug=slugify(trust[0]),
                company_name=trust[0],
                description=trust[8],
                start_production=trust[3],
                end_production=trust[4],
                abbr=trust[2],
                fund_name=trust[1],
                mesothelioma=mesothelioma,
                lung_cancer=lung_cancer,
                other_cancer=other_cancer,
                asbestosis=asbestosis,
                severe_asbestosis=severe_asbestosis,
                budget=budget_relation,
            )
            new_trust = Trust.objects.get(slug=slugify(trust[0]))
            new_trust.states.add(*relation_state)