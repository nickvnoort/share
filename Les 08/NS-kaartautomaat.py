def inlezen_beginstation(stations):
    beginstation = input('Geef begin station: ')
    while beginstation not in stations:
        beginstation = input('Niet goed, geef beginstation')
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Geef eind station: ')
    while eindstation not in stations:
        eindstation = input('Niet goed, geef eindstation')
    while stations.index(eindstation)< stations.index(beginstation):
        eindstation = input('Niet goed, geef eindstation')
    return eindstation

def omroepen_reis(station, beginstation, eindstation):
    nummerB = stations.index(beginstation) +1
    nummerE = stations.index(eindstation) +1
    Tussenstation = stations.index(beginstation)
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, nummerB))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, nummerE))
    print('de afstand bedraagt {} stations'.format(nummerE-nummerB))
    print('De prijs van je rijs is {} euro'.format((nummerE-nummerB)*5))
    print('je stapt in de trein in: {}'.format(beginstation))
    while Tussenstation < stations.index(eindstation):
        print('- {}'.format(Tussenstation))
        Tussenstation = Tussenstation + 1
    print('je stapt uit de trein in : {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal','Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosh','Eindhoven','Weert','Roermond','Sittard', 'Maastricht']
beginstation= inlezen_beginstation(stations)
eindstation= inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)