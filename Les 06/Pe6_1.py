def seizoen(maand):
    if maand >2 and maand <6:
        print('lente')
    elif maand >5 and maand < 9:
        print('zomer')
    elif maand > 8 and maand <12:
        print('herfst')
    elif maand >12:
        print('Dat kan niet joh!')
    elif maand <1:
        print('Ongemogelijk!')
    else:
        print('winter')

seizoen(eval(input('Wat is het nummer van de maand?: ')))