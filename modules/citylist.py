# encoding: utf-8

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.tripadvisor.se"

def get_cities_from_list(url):
    print "Open %s" % url
    cities = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    try: 
        list_items = soup.find("div", { "id": "CHILD_GEO_FILTER"})\
            .find_all("div", {"class": "filter"})[:-1]
        first_page = True
        next_page = BASE_URL + soup.find("div", { "id": "CHILD_GEO_FILTER"})\
            .find_all("div", {"class": "filter"})[-1]\
            .find("a")["href"]

    except:
        list_items = soup.find('ul', {'class':'geoList'}).find_all('li')
        first_page = False
        try:
            next_page = BASE_URL + soup.find("a", class_="sprite-pageNext")["href"]
        except:
            next_page = None

    for li in list_items:
        link_tag = li.find("a")
        city = {}
        if first_page:
            city["name"] = link_tag.find("span",{"class":"filter_name"})\
                .text\
                .replace(u"Saker att göra i ","")
        else:
            city["name"] = link_tag.text.replace(u"Sevärdheter i ","")
        city["url"] = BASE_URL + link_tag["href"]
        cities.append(city)
    
    print "Found %s cities" % len(cities)

    return {
        "data": cities,
        "next_page_url": next_page,
    }
