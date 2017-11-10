zin = 'all animals are equal but some animals are more equal then others'
woorden = zin.split()
woordenteller = {}


for woord in woorden:
    if woord in woordenteller.keys():
        woordenteller[woord] += 1
    else:
        woordenteller[woord] = 1
print(woordenteller)

# woord (variable) 'komt' woordenteller(woord) (variable) 'keer voor'

for woord in woordenteller:
    print('{:8} komt {} keer voor.' .format(woord,6 woordenteller[woord]))