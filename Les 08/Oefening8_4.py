woord = input('voer een woord in: ')
for letter in woord:
    code = ord(letter)
    print('{} {} {:x} {:b}'.format(letter, code, code, code))