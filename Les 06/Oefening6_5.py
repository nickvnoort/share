tabel = [[4, 7, 2, 5],[5, 1, 9, 2],[3, 2, 6, 1]]
for rij in range(3):
    for kolom in range(4):
        print( tabel[rij][kolom], end = ' ')
    print()

print('.....')


3 is len(tabel)
3 is len(tabel[0])

for rij in range(len(tabel)):
    for kolom in range(len(tabel[0])):
        print(tabel[rij][kolom], end = '')
    print()

print('.....')

aantalrijden = len(tabel)
aantalkolommen = len(tabel[0])
for rij in range(aantalrijden):
    for kolom in range(aantalkolommen):
        print(tabel[rij][kolom], end = '')
    print()