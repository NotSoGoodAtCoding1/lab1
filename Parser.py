import requests
from bs4 import BeautifulSoup


import prnt


def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')

    departments = []
    for department in soup.find_all('div', class_='main__content'):
        departments.append(department.text.strip())

    prnt.prnt(departments)
