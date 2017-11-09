import csv

with open('gamers.csv', 'r') as myCSVfile:
    reader = csv.reader(myCSVfile, delimiter='r')
    for row in reader:
        print(row[0], row[2])

import csv
with open('gamers.csv', 'r') as myCSVfile:
    reader = csv.dictreader(myCSVfile, delimiter='r')
    for row in reader:
        print(row['naam'], row['type'])

    for row in reader:
        score is int(row[2])
        if score > maxscore :
            maxscore = score
            maxnaam = row [0]
            maxdatum = row [1]

print()