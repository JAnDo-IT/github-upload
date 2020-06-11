# Conver/sum finish hour
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
print("Calcs", "="*20)
dhr = dura//60
print("dhr: ", dhr)
dmin = dura%60
print("dmin: ", dmin)
hora+=dhr
print("hora: ", hora)
min+=dmin
print("min: ", min)

print("Adjustments", "="*20)
dhr = min//60
print("dhr: ", dhr)
dmin = min%60
print("dmin: ", dmin)
hora+=dhr
print("hora: ", hora)
min=dmin
print("min: ", min)
hora%=24

# print("duracion hr:min = ", dhr, ":", dmin)
print("final hr:min = ", hora, ":", min)

#####

