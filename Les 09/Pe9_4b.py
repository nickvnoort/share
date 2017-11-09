import csv

with open('producten.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter= ',')
    maxprijs = 0
    for row in reader:
        prijs = int(row['prijs'])
        if prijs > maxprijs:
            maxprijs = prijs
            maxnaam = row ['naam']