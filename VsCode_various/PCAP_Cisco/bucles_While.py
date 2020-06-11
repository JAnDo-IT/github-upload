numeroSecreto = 777

# print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""" #)

"""
jugador=int(input("Ingresa un número entero: "))

while jugador != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    jugador=int(input("Ingresa otro número entero: "))

print()
print(jugador)
print("¡Bien hecho, muggle! Eres libre ahora")
print()
"""
"""
lim= 10
paso=0

for i in range(2, lim, 2):
    paso+=2
    print(i, paso)

print()
"""
#No imprime nada al igual que range(), ie vacio
for i in range(1, 1):
    print("El valor de i es actualmente", i)
#Ni aqui
for i in range(2, 1):
    print ("El valor de i es actualmente", i)

#Descendente no se puede

#Potencias de 2
"""
pow = 1
for exp in range(10):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 

print()
""" 
"""
import time

    # Escribe un ciclo for que cuente hasta cinco.
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    # Cuerpo del ciclo - uso: time.sleep (1)

# Escribe una función de impresión con el mensaje final.

for mis in range(1,6):
    print (mis, "Mississippi")
    time.sleep(1)

print()
"""

# break - ejemplo
"""
print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")
"""

# While con Break
"""
numeroMayor = -99999999
contador = 0

print("-"*15)

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

print("-"*15)
"""
#While con Continue
"""
numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    #if numero == -1:
    #    continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 
"""
#Ejercicio pal clave
"""
clave="chupacabra"
pal=input("Palabra: ")

while True: 
    if pal == clave:
        break
    pal=input("Palabra: ")

print("¡Has dejado el ciclo con éxito")
print()
"""

#Devorador de vocales
"""
palabraSinVocal = ""

userWord = input("Palabra: ")
userWord = userWord.upper()
vocales = "AEIOU"

for pal in userWord:
    if pal == 'A' or pal == 'E' or pal == 'I' or pal == 'O' or pal == 'U':
        continue
    else:
        palabraSinVocal += pal
        
#print(pal)
print(palabraSinVocal)
"""

print()
#Calcular Altura de la pirámide:
"""
altura=1    # 1, 2, 3, 4
i=2         # 2, 3, 4, 5
acum=1      # 1, 3, 6, 10
bloques = int(input("Ingrese el número de bloques:")) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#
if bloques>= 1:
    while (acum+i) <= bloques:
        altura+=1
        acum+=i
        i+=1
        # print(i, altura, acum)
    print("La altura de la pirámide:", altura)
else:
    print("Num bloques no permitido")
"""

# En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado)
# 1. num >= 0
# 2. par c0 = c0/2
# 3. impar: 3 * c0 + 1
# 4. si c0 != 1 regresa a 2

"""
c0 = int(input("num Lothar: "))
pasos= 0

if c0 > 0:
    if c0 == 1 :
        c0 = 3 * c0 + 1
        print(int(c0))
        pasos=1
    
    while c0 != 1 :
        if c0 % 2 == 0 :
            c0/=2
        else:
            c0 = 3 * c0 + 1
        pasos += 1
        print(int(c0))
    print("pasos= ", pasos)
else:
    print("Numero no válido")
"""
print()

#inverso
for i in range(6, 1, -2):
    print(i, end=" ") # salidas: 6, 4, 2

print()

newpal=""
# reemplazar 0s
for digit in "0165031806510":
    if digit == "0":
        newpal+="x"
        continue
    newpal+=digit
print(newpal)

print("Op 2")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

# 10001
# R: 01000 = 8
# L: 100010 = 68
# x= 0100
# y= 0001
# a= 0000 = 0
# b= 0101 = 5
# c= 1011 = 7 x ====> -5
# d= (0101) = 0110 = 6 ===> 1
# e= 0001 = 1
# f= 10000 = 16
