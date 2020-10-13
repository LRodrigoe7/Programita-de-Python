import random

diff= int(input("Seleccione la Dificultad: 1-Facil, 2-Medio, 3-Dificil."))
if diff == 1:
    intentos = 9
elif diff == 2:
    intentos = 6
else:
    intentos = 3

print('¡Hola! ¿Cómo te llamas?')

miNombre = input()
número = random.randint(1, 20)

print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')
x = 0
while x < intentos:

    print('Intenta adivinar.')
    estimación = input()
    estimación = int(estimación)
    
    if estimación < número:
        print('Tu estimación es muy baja.') 

    if estimación > número:
        print('Tu estimación es muy alta.')

    if estimación == número:
        break
    x += 1

if estimación == número:
    x = str(x)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + x + ' intentos!')

if estimación != número:
    número = str(número)

    print('Pues no. El número que estaba pensando era ' + número)
    print("Bad Luck My Brother")
    main
