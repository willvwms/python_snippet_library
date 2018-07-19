import csv

with open("people.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(dict(row))

csvFile.close()
