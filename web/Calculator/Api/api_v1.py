# from rest_framework.generics import ListAPIView,RetrieveAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from ShipsShipyards.models import *
# from ShipsShipyards.serializers import *
# from django.db.models import  Max
# from ShipsShipyards.zipcode import *
# from ShipsShipyards.source import calculateCompensation
# import uuid
#
#
# class DiseaseAPIView(ListAPIView):
#     queryset = Disease.objects.all()
#     serializer_class = DiseaseAPISerializer
#
#
# class SOLApi(APIView):
#     def post(self, request):
#         state = State.objects.get(abbr=request.data["resident_state"])
#         return Response({"year_death":state.years_from_death,
#                          "year_diagnosed": state.years_from_diag,
#                          })
#
#
# class JobAPI(APIView):
#     def post(self, request):
#         jobs = Job.objects.filter(jobgroup__name__in=request.data["groups"]).distinct()
#         return Response(JobAPISerializer(jobs, many=True).data)
#
#
# class JobIndustryAPIView(APIView):
#     def post(self, request):
#         state = request.data["state"]
#         trusts = Trust.objects.filter(states__abbr=state).distinct()
#         industry = JobIndustry.objects.filter(trust__in = trusts ).distinct()
#         return Response(JobIndustryAPISerializer(industry, many=True).data)
#
#
# class JobGroupAPI(APIView):
#     def post(self, request):
#         groups = JobGroup.objects.filter(jobindustry__name__in=request.data["industry"]).distinct().order_by('name')
#         return Response(JobAPISerializer(groups, many=True).data)
#
#
#
#
#
# class YearWorkApi(APIView):
#     def post(self, request):
#         state_abbr=[item["abbr"] for item in request.data["work_state"]]
#         year_to = Trust.objects.filter(states__abbr__in=state_abbr).aggregate(Max('end_production'))
#         return Response({"year":year_to["end_production__max"]})
#
#
# class StateGetAPIView(ListAPIView):
#     queryset = State.objects.all().order_by("name")
#     serializer_class = StateGetAPISerializer
#
#
# class StateByZipAPIView(APIView):
#
#     def post(self, request):
#         try:
#             state_by_zip, city = get_state(request.data["zipcode"])
#             state = State.objects.get(abbr=state_by_zip)
#             return Response({"city":city, "abbr":state.abbr, "name":state.name})
#         except:
#             return Response({"city": "", "abbr": "", "name": ""})
#
#
#
# class StatePostAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         state = State.objects.get(abbr=request.data["state"])
#         return Response(StatePostAPIView(state).data)
#
#
# class UpDateClientInfo(APIView):
#
#     def post(self, request):
#         try:
#             token = request.headers['Token']
#         except:
#             return Response({"status":False})
#         client_token = token
#         try:
#             client = Client.objects.get(token=client_token)
#             field = client.disease.name.lower().replace(" ","_")
#
#             returnData = {
#                 "status":True,
#                 "disease": client.disease.name,
#                 "compensation":{
#                     "ir": client.verdict_ir,
#                     "avg": client.verdict_avg,
#                     "er": client.verdict_er,
#                 },
#                 "trusts":[{
#                     "name":trust.company_name,
#                     "fund_name": trust.fund_name,
#                     "compensation":{
#                         "ir": int(getattr(trust, field).compensation_ir * trust.mesothelioma.ratio / 100),
#                         "avg": int(getattr(trust, field).compensation_avg * trust.mesothelioma.ratio / 100),
#                         "er": int(getattr(trust, field).compensation_er * trust.mesothelioma.ratio / 100),
#                     },
#                     "budget":{
#                         "initial":trust.budget.initial_amount,
#                         "available":trust.budget.available_amount,
#                     },
#                     "logo":trust.logo.url
#                 }
#                 for trust in client.trusts.all()]
#
#             }
#             return Response(returnData)
#         except:
#             return Response({"status": False})
#
#
#
#
#
# class GetClientInfo(APIView):
#
#     def get(self, request):
#         try:
#             token = request.headers['Token']
#         except:
#             return Response({"status":False})
#         client_token = token
#         try:
#             client = Client.objects.get(token=client_token)
#             field = client.disease.name.lower().replace(" ","_")
#             returnData = {
#                 "status":True,
#                 "deceased":client.deceased,
#                 "diagnosed":client.diagnosed,
#                 "disease": client.disease.name,
#                 "lives":client.lives,
#                 "victim":client.victim,
#                 "smoker":client.smoker,
#                 "phone":client.phone,
#                 "about":client.additional_info,
#                 "compensation":{
#                     "ir": client.verdict_ir,
#                     "avg": client.verdict_avg,
#                     "er": client.verdict_er,
#                 },
#                 "state":{
#                     "name":client.resident_state.name,
#                     "abbr":client.resident_state.abbr,
#                 },
#             }
#             return Response(returnData)
#         except:
#             return Response({"status": False})
#
#
# class AddClientAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             disease = Disease.objects.get(name=request.data['disease'])
#             victim = request.data['victim']
#             lives = request.data['lives']
#             additional_info = request.data['additional_info']
#             phone = request.data['phone']
#             smoker = request.data['smoker'].lower()
#             abbr = [item["abbr"] for item in request.data["work_states"]]
#             work_state = State.objects.filter(abbr__in = abbr)
#
#             trust_abbr_set = set()
#             industry_set = set()
#             for state in request.data["work_states"]:
#                 trust_list = Trust.objects.filter(industries__name__in=state["industry"],
#                                                   states__abbr=state["abbr"]).distinct()
#                 trust_abbr_set = trust_abbr_set | set([trust.abbr for trust in trust_list])
#                 industry_set = industry_set | set(state["industry"])
#             industries = JobIndustry.objects.filter(name__in=industry_set)
#             trusts = Trust.objects.filter(abbr__in=trust_abbr_set)
#             deceased = request.data["deceased"]
#             diagnosed = request.data["diagnosed"]
#             resident_state = State.objects.get(abbr = request.data['resident_state'])
#             verdict_ir = calculateCompensation(trusts, disease, smoker, "ir")
#             verdict_avg = calculateCompensation(trusts, disease, smoker, "avg")
#             verdict_er = calculateCompensation(trusts, disease, smoker, "er")
#             if (Client.objects.all().count()):
#                 client_token = str(uuid.uuid4())+str(Client.objects.latest("pk").pk)
#             else:
#                 client_token = str(uuid.uuid4()) + "1"
#
#         except Exception as e:
#             print(e)
#             return Response({"status": False})
#         try:
#             new_client = Client.objects.create(
#                 disease = disease,
#                 victim = victim,
#                 lives = lives,
#                 additional_info = additional_info,
#                 phone = phone,
#                 smoker = smoker,
#                 resident_state = resident_state,
#                 verdict_ir = verdict_ir,
#                 verdict_avg = verdict_avg,
#                 verdict_er = verdict_er,
#                 token = client_token,
#                 deceased=deceased,
#                 diagnosed=diagnosed,
#             )
#             new_client.work_state.add(*work_state)
#             new_client.industries.add(*industries)
#             new_client.trusts.add(*trusts)
#             new_client.save()
#             return Response({
#                 "status": True,
#                 "token": new_client.token,
#             })
#         except Exception as e:
#             print(e)
#             return Response({"status": False})