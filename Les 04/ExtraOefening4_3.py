def eindbedrag (bedrag, percentage):
    nieuwbedrag = bedrag + percentage * bedrag /100
    print(nieuwbedrag)

bedrag = eval(input('Geef bedrag: '))
percentage = eval(input('Geef percentage: '))
eindbedrag(bedrag, percentage)
