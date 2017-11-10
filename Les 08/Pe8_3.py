def code(invoerstring):
    nieuwestring = ''
    for kar in invoerstring:
        nieuweASCII = ord(kar) + 3
        nieuwekar = chr(nieuweASCII)
        nieuwestring += nieuwekar
    return nieuwestring

naam = input('Geef naam: ')
beginstation = input('Geef begin station: ')
eindstation = input('Geef eindstation: ')
invoerstring = naam + beginstation + eindstation

print(code(invoerstring))