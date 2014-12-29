#!/usr/bin/python
import csv, json, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: csv-to-json.py file.csv')
fileIn = sys.argv[1]
try:
	fileOut = sys.argv[2]
except:
	fileList = [fileIn.split('.')[0], 'json']
	fileOut = ".".join(fileList)

data = csv.reader(open(fileIn, 'rU'), delimiter=',')

# get header row
fieldnames = data.next()

# get number of columns
fieldnames_len = len(fieldnames)

jsonList = []
i = 0

for row in data:
	# add an empty dict to the list
	jsonList.append({})

	for j in range(0, len(row)):
		jsonList[i][fieldnames[j]] = row[j]

	# what if last cells are empty?
	for j in range(len(row), fieldnames_len):
		jsonList[i][fieldnames[j]] = ""

	i = i + 1

with open(fileOut, 'w') as outfile:
	json.dump(jsonList, outfile, sort_keys=True, indent=4, ensure_ascii=False)
sys.exit()