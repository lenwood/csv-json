#!/usr/bin/python
import json, sqlite3, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-sqlite.py file.json')
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'db']
filename_out = ".".join(filename_list)

# read in the filename
input = open(filename_in)
jsonData = json.load(input)
input.close()

# structure the json data
jsonColumns = str(",".join(list(jsonData[0].keys())))
jsonValues = [':{0}'.format(i) for i in jsonData[0].keys()]
jsonValues = ", ".join(jsonValues)

# assemble the SQL query
query = ["INSERT INTO jsonFile VALUES (", jsonValues, ")"]
queryString = " ".join(query)

# establish connection to the database & execute the query
conn = sqlite3.connect(filename_out) # or use :memory: to put it in RAM
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS jsonFile(" + jsonColumns + ")")
	cur.executemany(queryString, jsonData)
