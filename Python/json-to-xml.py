#!/usr/bin/python
import json, dicttoxml, sys

# pass the filename as an argument when calling this script
if len(sys.argv) < 2:
	sys.exit('Usage: json-to-xml.py file.json')
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'xml']
filename_out = ".".join(filename_list)

# read the json file filename in
input = open(filename_in)
data = json.load(input)
input.close()

# convert to xml
xml = dicttoxml.dicttoxml(data)

# write the xml file
with open(filename_out, "wb+") as outfile:
	outfile.write(xml)
