import csv, json, sys

# pass the filename as an argument when calling this script
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'json']
filename_out = ".".join(filename_list)

data = csv.reader(open(filename_in, 'rU'), delimiter=',')

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

with open(filename_out, 'w') as outfile:
	json.dump(jsonList, outfile, sort_keys=True, indent=4, ensure_ascii=False)
sys.exit()