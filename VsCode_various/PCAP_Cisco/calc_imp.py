# Cálculo de impuestos
"""
ingreso=float(input("Ingrese el ingreso anual:"))

#
# Coloca tu código aquí.
#
lim = 85528
imp = 0.0

if ingreso <= lim :
    imp = (ingreso * 0.18) - 556.02
else:
    imp = 14839.02 + ((ingreso - lim)*0.32) 

if imp < 0 :
    imp = 0.0

impuesto=round(imp, 0)
print("El impuesto es: ", impuesto, "pesos")
"""

"""
## Bisiestos
año = int(input("Introduzca un año:"))

mens = "No dentro del período del calendario gregoriano"

#
# Coloca tu código aquí.
#
if año >= 1582:
    if ( año % 4 ) != 0:
        mens = "Año común"
    if ( año % 100 ) != 0:
        mens = "Año bisiesto"
    if ( año % 4 ) != 0:
        mens = "Año común"
    else:
        mens = "Año bisiesto"

print(mens)

"""
x, y, z = 5, 10, 8

print(x, y, z, sep="--")
