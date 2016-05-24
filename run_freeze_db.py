import dataset

db_url = "sqlite:///data/tripadvisor.db"
db = dataset.connect(db_url)

dataset.freeze(db["attractions"].all(), filename="data/attractions.csv", format="csv")
