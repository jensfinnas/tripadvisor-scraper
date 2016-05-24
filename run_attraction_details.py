import dataset
from modules.attraction_page import scrape_attraction_page


db_url = "sqlite:///data/tripadvisor.db"
db = dataset.connect(db_url)
attractions = db["attractions"]

for row in attractions.all():
    url = row["url"]
    if "Attraction_Review" not in url:
        print "Delete %s" % url
        attractions.delete(url=url)
    else:
        details = scrape_attraction_page(url)
        details["url"] = url
        attractions.update(details, ["url"])
