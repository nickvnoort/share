getallenrij = [ 2, 4, 6, 8, 10, 9, 7]
x=0
for getal in getallenrij:
    if getal %3 == 0:
        x = x + 1
print ('Het aantal getallen deelbaar door 3 is : ' + str(x))