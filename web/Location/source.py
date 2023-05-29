from .models import *
import csv
from slugify import slugify

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VI': 'Virgin Islands',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming',
}

state_info = [
    {
        'name': 'Puerto Rico',
        'years_from_diag': 2,
        'years_from_death': 2
    },
  {
    'name': 'Alabama',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Alaska',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Arizona',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Arkansas',
    'years_from_diag': 5,
    'years_from_death': 5
  },
  {
    'name': 'California',
    'years_from_diag': 10,
    'years_from_death': 4
  },
  {
    'name': 'Colorado',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Connecticut',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Delaware',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Florida',
    'years_from_diag': 4,
    'years_from_death': 3
  },
  {
    'name': 'Georgia',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Hawaii',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Idaho',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Illinois',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Indiana',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Iowa',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Kansas',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Kentucky',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'Louisiana',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'Maine',
    'years_from_diag': 6,
    'years_from_death': 4
  },
  {
    'name': 'Maryland',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Massachusetts',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Michigan',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Minnesota',
    'years_from_diag': 6,
    'years_from_death': 4
  },
  {
    'name': 'Mississippi',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Missouri',
    'years_from_diag': 5,
    'years_from_death': 4
  },
  {
    'name': 'Montana',
    'years_from_diag': 6,
    'years_from_death': 4
  },
  {
    'name': 'Nebraska',
    'years_from_diag': 6,
    'years_from_death': 4
  },
  {
    'name': 'Nevada',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'New Hampshire',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'New Jersey',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'New Mexico',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'New York',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'North Carolina',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'North Dakota',
    'years_from_diag': 6,
    'years_from_death': 4
  },
  {
    'name': 'Ohio',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'Oklahoma',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Oregon',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Pennsylvania',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'Rhode Island',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'South Carolina',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'South Dakota',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Tennessee',
    'years_from_diag': 3,
    'years_from_death': 3
  },
  {
    'name': 'Texas',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Utah',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Vermont',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Virginia',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Washington',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'District of Columbia',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'West Virginia',
    'years_from_diag': 4,
    'years_from_death': 4
  },
  {
    'name': 'Wisconsin',
    'years_from_diag': 4,
    'years_from_death': 3
  },
  {
    'name': 'Wyoming',
    'years_from_diag': 4,
    'years_from_death': 3
  }
]

def upload_state():
  for abbr, name in states.items():
    State.objects.update_or_create(name=name, abbr=abbr)
  for inf in state_info:
    obj = State.objects.get(name=inf['name'])
    obj.years_from_diag = inf['years_from_diag']
    obj.years_from_death = inf['years_from_death']
    obj.save()


def upload_city():
  file = open("Location/upload/ZIPFlorida.tsv", "r")
  list_row = list(csv.reader(file, delimiter="\t"))
  for index,row in enumerate(list_row):
    print(index)
    city = row[0]
    state_abbr = row[1]
    state = State.objects.get(abbr=state_abbr)
    nr = 0
    if row[2].isnumeric():
      nr = int(row[2])
    list_zips = [zip for zip in row[3].split(" ") if zip.isnumeric()]
    for zip in list_zips:
      ZipCode.objects.update_or_create(code=str(zip))
    zips = ZipCode.objects.filter(code__in=list_zips)
    if City.objects.filter(search_slug=slugify(city +" "+state.abbr)).exists():
      pass
    else:
      c = City.objects.create(
          name=city,
          state=state,
          number_of_population=nr,
        )
      c.zipcode.add(*zips)





