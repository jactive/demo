import csv as csv
csvfile = file('data.csv')
reader = csv.reader(csvfile)
for i in range(6):
   reader.next()
for line in reader:
   print line[1]

csvfile.close()
