# getallenrij= [2, 4, 6, 8, 10, 9, 7]
# Zoekgetal=eval(input('Geef een getal op: '))
# gevonden=False
#
# for getallen in getallenrij:
#     if getallen==Zoekgetal:
#         gevonden=True
#
# if gevonden==True:
#     print('Het getal dat je hebt ingevuld komt voor in de getallenrij')
# else:
#     (print('Get getal dat je hebt ingevuld komt niet voor in de getallenrij'))

getallenrij = [2, 4, 6, 8, 10, 9, 7]
zoekgetal = eval(input('Voer een getal in: '))
print(zoekgetal)
gevonden = False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True
if gevonden == True:
    print('Het zoekgetal zit in de getallenrij')
else:
    print('Het zoekgetal zit niet in de getallenrij')
