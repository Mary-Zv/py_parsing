#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного
# пользователя, сохранить JSON-вывод в файле *.json.

#https://docs.github.com/en/rest/reference/repos#list-repositories-for-a-user

#https://api.github.com/users/username/repos - список репозиториев конкретного пользователя

import requests
import json
def repo_list(url, user):
    '''Функция получает список репозиториев и записывает их назания в json файл'''
    response = requests.get(f'{url}/users/{user}/repos')

    #Создаем пустой список куда и будем добавлять название репозитория
    repository_list = []
    for i in response.json():
        repository_list.append(i['name'])
        print(i['name']) #выводим в терминал только название репозитория

    with open('repository_name_list.json', 'w') as file:
        json.dump(repository_list, file)

    with open('full_response.json', 'w') as file:
        json.dump(response.json(), file)

repo_list('https://api.github.com', 'mary-zv')




