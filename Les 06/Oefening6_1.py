gewicht = eval(input('Wat is je gewicht: '))
lengte = eval(input('Wat is jou lengte: '))
BMI = gewicht / (lengte**2)

if BMI <= 18.5:
    print('Jammer joh, je hebt ondergewicht')

elif (BMI > 18.5) and (BMI < 25):
    print('lekkah bezig houde zoo')

else:
    print ('dikzak')
