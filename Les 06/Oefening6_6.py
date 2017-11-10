lijst = [[0, 156, 0, 0],[34, 0, 0, 0],[23, 123, 0, 34]]

aantalrijen = len(lijst)
aantalkolommen = len(lijst[0])
aantalpixels = 1

for rij in range(aantalrijen)):
    for kolom in range(aantalkolommen) :
        if lijst[rij][kolom] > 0:
            print(lijst[rij][kolom], end = '')
        print()