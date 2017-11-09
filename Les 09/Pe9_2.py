import csv

with open('newfile.csv', 'w', newline = '') as myCSVFile :
    writer  = csv.writer(myCSVFile, delimiter = ',')
    while True:
        naam = input('Wat is je naam: ')
        if naam == 'einde' :
            break
        voorl = input('Wat zijn je voorletters: ')
        if voorl == 'einde' :
            break
        geboortedatum = input('Wat is je geeboortedatum: ')
        if geboortedatum == 'einde' :
            break
        email = input('Wat is je email: ')
        if email == 'einde' :
            break

        writer.writerow((naam, voorl, geboortedatum, email))