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
