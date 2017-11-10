def inlezen_beginstation(stations):
    beginstation = input('Geef beginstation:')
    while beginstation not in stations:
        beginstation = input('Niet correct, geef beginstation:')
    return beginstation

def inlezen_eindstation(stations,beginstation):
    eindstation = input('Geef eindstation:')
    while eindstation not in stations:
        eindstation = input('Niet correct, geef eindstation')
    while stations.index(eindstation) < stations.index(beginstation):
        eindstation = input('Niet correct, geef eindstation')
    return eindstation

def omroepen_reis(stations,beginstation,eindstation):
    nummerB = stations.index(beginstation)+1
    nummerE = stations.index(eindstation)+1
    print('Het beginstation {} is het {} station in het traject.'.format(beginstation, nummerB))
    print('Het eindstation {} is het {} station in het traject.'.format(eindstation, nummerE))
    afstand = nummerE - nummerB
    print('De afstand bedraagt {} station(s).'.format(afstand))
    prijs = 5 * afstand
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    for index in range(nummerB,nummerE-1):
        print(' - {}'.format(stations[index]))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdentraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation= inlezen_beginstation(stations)
eindstation= inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)