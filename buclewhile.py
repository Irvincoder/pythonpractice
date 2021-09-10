"""x = 0
while x <= 100:
    print(x)
    x = x + 10"""

"""x = 1
n = int(input("Ingrese el numero hasta donde llegara\n"))
while x <= n:
    print(x)
    x = x + 1"""    

"""x = 1
suma = 0
n = int(input("Cuantas notas ingresara\n"))
while x <= n:
    notas = int(input("Ingrese notas\n"))
    suma = suma + notas
    x = x + 1
promedio = suma / 3
print("La suma de las notas es: "+str(suma))
print("El promedio de las notas es: "+str(promedio))"""

x = 1
edad = 0
n = int(input("Cuantas personas ingresara\n"))
while x <= n:
    edades = int(input("Ingrese edades\n"))
    if edades >= 25 and edades <= 40:
        edad = edad + 1
    x = x + 1
print("La cantidad de personas que pueden ingresar son: "+str(edad))