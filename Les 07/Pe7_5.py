namendict = {}
naam = input('volgende naam: ')
while naam != '' :
    if naam in namendict:
        namendict[naam] += 1
        print()

    else :
        namendict[naam] = 1