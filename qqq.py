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
        if link.find("news") != None:
            study.append(link['href'])

    page_number += 1

print(study)
    
for link in study:
    #navegador.get(link)

    
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')

    page_content = navegador.page_source

    #site = BeautifulSoup(page_content, 'html.parser')


    titles  = soup.select('h3+ .row .balloon:nth-child(1) p').get_text()
    print(titles)
    study_types = soup.select('h3+ p').get_text()
    print(study_types)
    dates = soup.select('.value:nth-child(3)').get_text()
    print(dates)
    ids = soup.select('ul:nth-child(15) .label+ .value').get_text()
    print(ids)
    conditions = soup.select('ul:nth-child(19)li:nth-child(1).balloon+.balloon p').get_text()
    print(conditions)
    names = soup.select('.subset+.subset.fn').get_text()
    print(names)
    cities = soup.select('.subset+.subset.locality').get_text()
    print(cities)
    countries = soup.select('.subset+ .subset .country-name').get_text()
    print(countries)
    phones = soup.select('.subset+.subset.tel').get_text()
    print(phones)
    emails = soup.select('.subset+.subset.email').get_text()
    print(emails)
    institutions = soup.select('.subset+.subset.org').get_text()
    print(institutions)
    
    juju = str(titles) + ";" + str(study_types) + ";" + str(dates) + ";" + str(ids) + ";" + str(conditions) + ";" + str(names) + ";" + str(cities) + ";" + str(countries) + ";" + str(phones) + ";" + str(emails) + ";" + str(institutions) + ";" + str(link)
    print(juju) 
    rebec.append(juju)

#tentativa falha de adicionar um cabeçalho
header = "titles" + ";" + "study_types" + ";" + "dates" + ";" + "ids" + ";" + "conditions" + ";" + "names" + ";" + "cities" + ";" + "countries" + ";" + "phones" + ";" + "emails" + ";" + "institutions"
#fim da tentativa falha de adicionar um cabeçalho

with open('rebec.csv', 'a', newline='') as f:
    write = csv.writer(f)
    # descomentar para testar header
    write.writerow(header)
    write.writerows(rebec)