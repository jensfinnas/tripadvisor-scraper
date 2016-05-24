
import dataset
from modules.attractionlist import *
from modules.utils import iterate_paginated_lists, DictList

db_url = "sqlite:///data/tripadvisor.db"
db = dataset.connect(db_url)
cities = db["cities"]

for row in cities.all():
    data = DictList()
    data.set_db(db_url)
    data += iterate_paginated_lists(get_attractions_from_list, row["url"])
    data.to_db("attractions", ["url"])
