#Basics Lists
listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

print(listaSombrero)
print("Long lista: ", len(listaSombrero))

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.
# sust = int(input("Num to replace: "))
sust=21

listaSombrero[2] = sust

print(listaSombrero)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del listaSombrero[-1]
print(listaSombrero)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Long lista: ", len(listaSombrero))

# print(listaSombrero)

## append() e insert() ------------------------
print("Append() e insert() ")
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

#
numeros.insert(1,333)

print(len(numeros))
print(numeros)

# Empty Lists -- Check the reverse
miLista = [] # creando una lista vacía

for i in range (5):
    #miLista.append (i + 1)
    miLista.insert(0, i + 1)

print(miLista)

#### Acumuladores  -----------------------
miLista = [10, 1, 8, 3, 5]
suma = 0

print("**" * 5, "Acumuladores", "**" * 5)
print(miLista)

# for i in range(len(miLista)):
#    suma += miLista[i]

for i in miLista:
    # print(suma)
    suma += i
    print(i)

print(suma)

### Intercambio escalares ------------------
variable1 = 1
variable2 = 2

print("Valores Iniciales: ")
print("variable1= ", variable1)
print("variable2= ", variable2)

variable1, variable2 = variable2, variable1

print("Intercambio: ")
print("variable1= ", variable1)
print("variable2= ", variable2)

## INTERCAMBIANDO VALORES
miLista = [10, 1, 8, 3, 5]

# Manual
miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print("mi Lista1")
print(miLista)

print("mi Lista2")
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista)

## EJERCICIO
"""
Escenario
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.
La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).

Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:
Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
"""
# paso 1
"""
beatles=[]
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    band = input("Agrega miembro: ")
    beatles.append(band)

print("Paso 3:", beatles)

# etapa 4
del beatles[-2]
print("Paso 4.1:", beatles)
del beatles[-1]
print("Paso 4.2:", beatles)


# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
"""

################### Lab 1
print()
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("La lista con elementos duplicados:")
print(miLista)

# Eliminar duplicados
rec = len(miLista)
unicos=[]
unicos.append(miLista[0])

for i in range(rec):
    if miLista[i] not in unicos:
        unicos.append(miLista[i])

print("La lista solo con elementos únicos:")
print(unicos)
print()

# Ejem 1
PEON_BLANCO = "W"
fila = [PEON_BLANCO for i in range(8)]
print("Fila de peones blancos ajedrez")
print(fila)
# Ejemp Potencias dos
dos = [2 ** i for i in range(8)]
print("Potencias dos")
print(dos)
# Ejem 2
cuadrados = [x ** 2 for x in range(10)]
print("Cuadrados")
print(cuadrados)
probabilidades = [x for x in cuadrados if x % 2 != 0]
print("Impares")
print(probabilidades)

print()

tablero  = []
EMPTY = "W"

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append(fila)

print(tablero)
print()
tablero1 = [[EMPTY for i in range(8)] for j in range(8)]
print(tablero1)
print()

#And now .... 
EMPTY = "-"
TORRE = "TORRE"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)

########## Temperaturas cada hora en un mes por dia
temps = [[0.0 for h in range(24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

suma = 0.0

for day in temps:
    suma += day[11]

promedio= suma / 31

print()
print("Temperatura promedio al mediodía:", promedio)

temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print()
print("La temperatura más alta fue:", mas_alta)

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# la matriz se actualiza mágicamente aquí
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, " fueron los días calurosos.")

### Vacantes en hotel

habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]

vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1

print()
print("Vacantes en el hotel: ", vacante)
print()
