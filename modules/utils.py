#encoding: utf-8
import dataset
import csvkit as csv

class DictList(list):
    def to_csv(self, file_name):
        headers = self[0].keys()
        with open(file_name, 'wb') as output_file:
            print "Write %s row to %s" % (len(self), file_name)
            dict_writer = csv.DictWriter(output_file, headers)
            dict_writer.writeheader()
            dict_writer.writerows(self)
  
    def set_db(self, db_url):
        self.db = dataset.connect(db_url)

    def to_db(self, table, match_keys):
        print "Add %s rows to %s" % (len(self), table)
        for row in self:
            self.db[table].upsert(row, match_keys)

def iterate_paginated_lists(function, starting_url):
    next_page_url = starting_url
    data = []
    while next_page_url:
        d = function(next_page_url)
        data += d["data"] 
        next_page_url = d["next_page_url"]
    print "Found a total of %s items" % len(data)

    return data

def parse_float(string):
    return float(string.replace(" ","").replace(u" ","").replace(",","."))

def parse_int(string):
    return int(parse_float(string))