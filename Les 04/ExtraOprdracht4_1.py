temperatuur = eval(input('Hoe warm is het vandaag: '))

if temperatuur  <= 0:
    print('Het vriest')
elif temperatuur >0 and temperatuur <= 15:
    print('Het is best wel koud')
else:
    print('Het is best wel lekkah weer vandaag')