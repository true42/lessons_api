import requests
from pprint import pprint
import json

API_URL = 'https://api.hh.ru/vacancies'
PARAMS = {'text': 'Python'}
list_vacancy = []

first_response = requests.get(API_URL, params=PARAMS)


for i in range(first_response.json()['pages']+1):
    PARAMS['page'] = i
    response = requests.get(API_URL, params=PARAMS).json()
    try:
        for j in response['items']:
            vacancy = {'name': j['name'],
                       'salary': j['salary'],
                       'alternate_url': j['alternate_url'],
                       'website': 'HH'}
            list_vacancy.append(vacancy)
    except KeyError:
        # больше 2000 вакансий не дают без регистрации в api
        pprint(response['description'])


with open('vacancy.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(list_vacancy, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))

