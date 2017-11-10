def lang_genoeg(lengte):
    if lengte >= 120:
        print('je bent langgenoeg, je mag naar binnen')
    else:
        print('Helass, je bent niet langgenoeg, je mag niet naar binnen')

lang_genoeg(eval(input('Wat is je lengte in cm: ')))
