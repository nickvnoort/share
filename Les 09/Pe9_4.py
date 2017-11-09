import csv

with open('producten.csv', 'w', newline = '') as myCSVfile:
    writer = csv.writer(myCSVfile, delimiter = ',')
    writer.writerow(('artikelnummer','artikelcode','naam','voorraad','prijs'))
    while True:
        artikelnummer = input(' ')
        # if artikelnummer == stop :
        #     break

        artikelcode = input(' ')
        # if artikelcode == stop :
        #     break

        naam = input(' ')
        # if naam == stop :
        #     break
        voorraad = input(' ')
        # if voorraad == stop :
        #     break

        prijs = input(' ')
        # if prijs == stop :
        #     break

    writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))