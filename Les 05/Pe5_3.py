infile = open('kaartnummers.txt', 'r')

regels = infile.readlines()
print(regels)

hoogste = 0
len(regels)
print(len(regels))

for regel in regels:
    kaartinfo = regel.split(',')
    print(kaartinfo[0])


