import requests
from pprint import pprint
import json
import config

'''
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, 
сохранить JSON-вывод в файле *.json.
'''

GIT_API_URL = 'https://api.github.com'
USER = 'true42'

response = requests.get(f'{GIT_API_URL}/users/{USER}/repos')
j_data = response.json()

with open('repos.json', 'w') as f:
    f.write(json.dumps(j_data, sort_keys=True, indent=4, separators=(',', ': ')))

'''
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). 
Выполнить запросы к нему, пройдя авторизацию. 
Ответ сервера записать в файл.
'''

VK_API_URL = 'https://api.vk.com/method/'
METHOD = 'users.get'
V = '5.131'

user_ids = 'true42_ab'
fields = 'online'
PARAMS = {'user_ids': user_ids,
          'fields': fields,
          'access_token': config.TOKEN,
          'v': V
          }

x = requests.get(VK_API_URL + METHOD, params=PARAMS)

j_data2 = x.json()

pprint(j_data2)
