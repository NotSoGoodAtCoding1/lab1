import requests
from bs4 import BeautifulSoup

url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

departments = []
for department in soup.find_all('div', class_='main__content'):
    departments.append(department.text.strip())

with open('departments.txt', 'w') as f:
    f.write('\n'.join(departments))
print(departments)
