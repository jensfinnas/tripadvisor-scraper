# encoding: utf-8

import requests
from bs4 import BeautifulSoup
from utils import parse_float, parse_int
import pdb

BASE_URL = "https://www.tripadvisor.se"

def get_attractions_from_list(url):
    print "Open %s" % url
    attractions = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    list_items = soup.find("div", { "id": "FILTERED_LIST"})\
        .find_all("div", {"class": "entry"})

    try:
        next_page = BASE_URL + soup.find("a", class_="next")["href"]
    except:
        next_page = None

    for li in list_items:
        attraction = {}
        title_tag = li.find("div", { "class": "property_title" }).find("a")
        attraction["name"] = title_tag.text
        attraction["url"] = BASE_URL + title_tag["href"]
        attraction["rank"] = parse_int(li.find("div", class_="popRanking").text.strip().split(" ")[1])
        try:
            attraction["score"] = parse_float(li.find("img", class_="sprite-ratings")["alt"].split(" ")[0])
        except TypeError:
            attraction["score"] = None

        try:
            attraction["n_reviews"] = parse_int(li.find("span", class_="more").text.strip().split(" ")[0])
        except AttributeError:
            attraction["n_reviews"] = None
        print attraction
        attractions.append(attraction)
    
    print "Found %s attractions" % len(attractions)

    return {
        "data": attractions,
        "next_page_url": next_page,
    }