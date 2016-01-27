#!/usr/bin/python
import csv, json, os, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-csv.py /path/to/file.json')
fileIn = sys.argv[1]
fileOnly = os.path.basename(fileIn)
try:
	fileOut = sys.argv[2]
except IndexError:
	fileList = [fileIn.split('.')[0], 'csv']
	fileOut = ".".join(fileList)

# read in the json file
input = open(fileIn)
data = json.load(input)
input.close()

# write the output csv
with open(fileOut, "wb+") as file:
	csv_file = csv.writer(file)
	csv_file.writerow(data[0].keys())		# header row
	for item in data:
		csv_file.writerow(item.values())