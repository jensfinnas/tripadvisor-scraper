# encoding: utf-8

import requests
from bs4 import BeautifulSoup
from utils import parse_float, parse_int
import pdb


def scrape_attraction_page(url):
    print "Open %s" % url
        
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    grade_labels = [u"Utmärkt", u"Mycket bra", u"Medelmåttigt", u"Dåligt", u"Hemskt"]
    grade_tags = soup.find_all("div", class_="valueCount")
    grade_values = [parse_int(x.text) for x in grade_tags]
    data = dict(zip(grade_labels, grade_values))


    breadcrumb_tags = soup.find("ul", {"id": "BREADCRUMBS"}).find_all("li")
    try:
        data["county"] = [x.text.strip() for x in breadcrumb_tags if u"län" in x.text][0]
    except IndexError:
        data["county"] = None

    data["city"] = soup.find("div", {"class": "slim_ranking"}).find("a").text\
        .replace(u"saker att göra i","").strip()

    tags = [x.text for x in soup.find("div", {"class": "heading_details"}).find_all("a")]
    data["tags"] = "|".join(tags)

    print data

    return data

