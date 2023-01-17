import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from time import sleep
import csv

options = Options()

navegador = webdriver.Firefox(options=options)

site_base = 'https://ensaiosclinicos.gov.br/list/'
page_number = 1
study = []
rebec = []

while page_number <=1:
    site = site_base + str(page_number)

    navegador.get(site)

    page_content = navegador.page_source

    site = BeautifulSoup(page_content, 'html.parser')

    links = site.find_all('a', attrs={'class': 'title_link'})

    for link in links:
        study.append(link['href'])

    page_number += 1

print(study)
    
for link in study:
    navegador.get(link)

    page_content = navegador.page_source

    site = BeautifulSoup(page_content, 'html.parser')


    titles  = soup.select('li:nth-child(2) .balloon:nth-child(1) p')
    study_types = soup.select('h3+ p')
    dates = site.find('.value:nth-child(3)')
    ids = site.find('ul:nth-child(15) .label+ .value')
    conditions = site.find('span', attrs={'class': 'ul:nth-child(19)li:nth-child(1).balloon+.balloon p'})
    names = site.find('span', attrs={'class': '.subset+.subset.fn'})
    cities = site.find('span', attrs={'class': '.subset+.subset.locality'})
    countries = site.find('span', attrs={'class': '.subset+ .subset .country-name'})
    phones = site.find('span', attrs={'class': '.subset+.subset.tel'})
    emails = site.find('span', attrs={'class': '.subset+.subset.email'})
    institutions = site.find('span', attrs={'class': '.subset+.subset.org'})

    print(titles)
    print(study_types)
#tentativa falha de adicionar um cabeçalho
    header = "titles" + ";" + "study_types" + ";" + "dates" + ";" + "ids" + ";" + "conditions" + ";" + "names" + ";" + "cities" + ";" + "countries" + ";" + "phones" + ";" + "emails" + ";" + "institutions"
    rebec.append(header)
#fim da tentativa falha de adicionar um cabeçalho

    juju = str(titles) + ";" + str(study_types) + ";" + str(dates) + ";" + str(ids) + ";" + str(conditions) + ";" + str(names) + ";" + str(cities) + ";" + str(countries) + ";" + str(phones) + ";" + str(emails) + ";" + str(institutions)
    print(juju)
    rebec.append(juju)

with open('rebec.csv', 'a', newline='') as f:
    write = csv.writer(f)
    write.writerows(rebec)