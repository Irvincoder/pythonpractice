"""for x in range(0,10,2):
    print(x)"""

"""n = int(input("Ingrese el recorrido\n"))
suma = 0
for x in range(n):
    notas = int(input("Ingrese notas\n"))
    suma = suma + notas
print("La suma de las notas es: "+str(suma))"""

"""suma = 0
n = int(input("Ingrese el numero de vueltas\n"))
for x in range(n):
    notas = int(input("Ingrese notas\n"))
    suma = suma + notas
    promedio = suma / 3
if promedio >= 7:
    print("Pasastes")
else:
    print("No Pasastes")"""

cantidad = 0
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    if valor >= 1000:
        cantidad = cantidad + 1
print("Los valores mayores o iguales a 1000 son: "+str(cantidad))