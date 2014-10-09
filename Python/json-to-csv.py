#!/usr/bin/python
import csv, json, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-csv.py file.json')
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'csv']
filename_out = ".".join(filename_list)

# read in the json file
input = open(filename_in)
data = json.load(input)
input.close()

# write the output csv
with open(filename_out, "wb+") as file:
	csv_file = csv.writer(file)
	csv_file.writerow(data[0].keys())		# header row
	for item in data:
		csv_file.writerow(item.values())