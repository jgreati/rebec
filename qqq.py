import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import csv

options = Options()

navegador = webdriver.Firefox(options=options)

url = "https://ensaiosclinicos.gov.br/list/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

page_number = 1
study = []
rebec = []

while page_number <=1:
    site = url + str(page_number)
    print(site)
    navegador.get(site)

    page_content = navegador.page_source

    site = BeautifulSoup(page_content, 'html.parser')

    links = site.find_all('a', attrs={'class': 'title_link'})

    for link in links:
        #para tirar os news
        if link.find("news") == None:
            study.append(link['href'])
        
    page_number += 1

print(study)
    
for link in study:
    navegador.get(link)
    
    # res = requests.get(link)
    # soup = BeautifulSoup(res.text, 'html.parser')

    page_content2 = navegador.page_source
    soup = BeautifulSoup(page_content2, 'html.parser')
    # print (soup)

    # with open('html.txt', 'w', newline='') as f:
    #             write = csv.writer(f)
    #             write.writerows(soup)

    titles  = soup.select('h3+ .row .balloon:nth-child(2)')
    if len(titles) >0:
        titles = titles[0].get_text()
    else:
        titles = 'titulo_nao_encontrado'
    print("titles")
    print(titles)
    print("----------------")

    study_types = soup.select('h3+ p')
    if len(study_types) >0:
        study_types = study_types[0].get_text()
    else:
        study_types = 'study_types_nao_encontrado'
    print("study_types")
    print(study_types)
    print("----------------")

    dates = soup.select('.value:nth-child(3)')
    if len(dates) >0:
        dates = dates[0].get_text()
    else:
        dates = 'dates_nao_encontrado'
    print("dates")
    print(dates)
    print("-------------")

    ids = soup.select('ul:nth-child(15) .label+ .value')
    if len(ids) >0:
        ids = ids[0].get_text()
    else:
        ids = 'titulo_nao_encontrado'
    print('ids')
    print(ids)
    print("----------------")

    conditions = soup.select('ul:nth-child(19) li:nth-child(1) .balloon+ .balloon p')
    if len(conditions) >0:
        conditions = conditions[0].get_text()
    else:
        conditions = 'conditions_nao_encontrado'
    print('conditions')
    print(conditions)
    print("----------------")

    names = soup.select('.subset~ .subset+ .subset .fn')
    if len(names) >0:
        names = names[0].get_text()
    else:
        names = 'names_nao_encontrado'
    print('names')
    print(names)
    print("----------------")

    cities = soup.select('.subset~ .subset+ .subset .locality')
    if len(cities) >0:
        cities = cities[0].get_text()
    else:
        cities = 'cities_nao_encontrado'
    print('cities')
    print(cities)
    print("----------------")

    countries = soup.select('.subset~ .subset+ .subset .country-name')
    if len(countries) >0:
        countries = countries[0].get_text()
    else:
        countries = 'countries_nao_encontrado'
    print('countries')
    print(countries)
    print("----------------")

    phones = soup.select('.subset~ .subset+ .subset .tel')
    if len(phones) >0:
        phones = phones[0].get_text()
    else:
        phones = 'phones_nao_encontrado'
    print('phones')
    print(phones)
    print("----------------")

    emails = soup.select('.subset~ .subset+ .subset .email')
    if len(emails) >0:
        emails = emails[0].get_text()
    else:
        emails = 'emails_nao_encontrado'
    print('emails')
    print(emails)
    print("----------------")

    institutions = soup.select('.subset~ .subset+ .subset .org')
    if len(institutions) >0:
        institutions = institutions[0].get_text()
    else:
        institutions = 'institutions_nao_encontrado'
    print('institutions')
    print(institutions)
    print("----------------")

    juju = str(titles), str(study_types), str(dates), str(ids), str(conditions), str(names), str(cities), str(countries), str(phones), str(emails), str(institutions), str(link)
    print('juju')
    print(juju) 
    rebec.append(juju)

#tentativa falha de adicionar um cabeçalho
header = "titles", "study_types", "dates", "ids", "conditions", "names", "cities", "countries", "phones", "emails", "institutions"
#fim da tentativa falha de adicionar um cabeçalho

print('inicio_da_gravacao')
with open('rebec.csv', 'w', newline='') as f:
    write = csv.writer(f)
    # descomentar para testar header
    write.writerow(header)
    write.writerows(rebec)
print('fim_da_gravacao')