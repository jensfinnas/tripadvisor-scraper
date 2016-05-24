from modules.citylist import *
from modules.utils import DictList

url = "https://www.tripadvisor.se/Attractions-g189806-Activities-Sweden.html"
#url = "https://www.tripadvisor.se/Attractions-g189806-Activities-oa470-Sweden.html"


data = DictList(get_all_cities(url))
data.set_db("sqlite:///data/tripadvisor.db")
data.to_db("cities",["name"])
