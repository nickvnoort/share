def eindbedrag (bedrag, percentage):
    nieuwbedrag = bedrag + percentage * bedrag /100
    print(nieuwbedrag)

print(eindbedrag(eval(input('Hoe groot is je startbedrag? ')),eval(input('Hoe groot is het rentepercentage in %? '))))