import csv, sqlite3, sys

# pass the filename as an argument when calling this script
filename_in = sys.argv[1]
filename_list = [filename_in.split('.')[0], 'db']
filename_out = ".".join(filename_list)

# read the file
data = csv.reader(open(filename_in, 'rU'), delimiter=',')

# structure the csv data
csvHeaderRow = data.next()
csvHeaders = ", ".join(str(i) for i in csvHeaderRow)
csvValues = [":{0}".format(j) for j in csvHeaderRow]
csvValues = ", ".join(csvValues)

# build the query
query = ["INSERT INTO csvFile VALUES (", csvValues, ")"]
queryString = " ".join(query)

# connect to the database & execute the query
conn = sqlite3.connect(filename_out)
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS csvFile(" + csvHeaders + ")")
	cur.executemany(queryString, data)