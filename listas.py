"""lista = [1, 2, 3, 4, 5]
suma = 0
x = 0
while x < len(lista):
    suma = suma + lista[x]
    x = x + 1
print(lista)
print(suma)"""

"""lista = []
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    lista.append(valor)
print(lista)"""    

"""lista = []
n = int(input("Para finalizar ingrese 0\n"))
while n != 0:
    lista.append(n)
    n = int(input("Para finalizar ingrese 0\n"))
print(lista)"""    

"""lista = []
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    lista.append(valor)
mayor = lista[0]
for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]
print("Lista entera: "+str(lista))
print("Numero mayor de la lista: "+str(mayor))"""

"""lista = []
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    lista.append(valor)
menor = lista[0]
posicion = 0
for x in range(1,5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x
print("Lista completa: "+str(lista))
print("El numero menor de la lista es: "+str(menor))
print("Posicion: "+str(posicion))"""

"""nombres = []
edades = []
for x in range(5):
    nom = str(input("Ingrese nombre\n"))
    nombres.append(nom)
    eda = int(input("Ingrese edad\n"))
    edades.append(eda)
print("Nombres con mayor edad")
for x in range(5):
    if edades[x] >= 18:
        print(nombres[x], edades[x])"""

"""sueldos = []
for x in range(5):
    sueldo =int(input("Ingrese sueldos\n"))
    sueldos.append(sueldo)
print("Sueldos: "+str(sueldos))
for x in range(4):
    if sueldos[x] > sueldos[x + 1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1] = aux
print("Lista con el numero de sueldo odenado: "+str(sueldos))"""

"""sueldos = []
for x in range(5):
    sueldo = int(input("Ingrese sueldo\n"))
    sueldos.append(sueldo)
print("Sueldo: "+str(sueldos))
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x+ 1 ] = aux
print("Lista ordenada: "+str(sueldos))"""         

"""alumnos = []
notas = []
for x in range(5):
    alumno = str(input("Ingrese nombre del alumno\n"))
    alumnos.append(alumno)
    nota = int(input("Ingrese la nota del alumno\n"))
    notas.append(nota)
for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x + 1]:
            aux = notas[x]
            notas[x] = notas[x + 1]
            notas[x + 1] = aux
            aux = alumnos[x]
            alumnos[x] = alumnos[x + 1]
            alumnos[x + 1] = aux
print("Notas ordenadas de mayor a menor:")            
for x in range(5):
    print(alumnos[x],notas[x])"""

"""notas = [[10,9,8],[7,6,5],[4,3,2],[1,0]]
for x in range(len(notas[0])):
    print(notas[x])"""

"""lista = [[9,5,7,6,8], [3,6,4,9,1]]
suma1 = lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3] + lista[0][4]
print("La suma de primera lista: "+str(suma1))
suma2 = lista[1][0] + lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4]
print("La suma de segunda lista es: "+str(suma2))
suma1 = 0
for x in range(len(lista[0])):
    suma1 = suma1 + lista[0][x]
suma2 = 0    
for x in range(len(lista[1])):
    suma2 = suma2 + lista[1][x]
print(suma1)
print(suma2)            
for k in range(len(lista)):
    suma = 0
    for x in range(len(lista[k])):
        suma = suma + lista[k][x]
    print(suma)"""

"""nombres = []
notas = []
for x in range(3):
    nom = str(input("Ingrese nombre\n"))
    nombres.append(nom)
    nota1 = int(input("Ingrese nota1\n"))
    nota2 = int(input("Ingrese nota2\n"))
    notas.append([nota1,nota2])
for x in range(3):
    print(nombres[x], notas[x][0], notas[x][1])"""

"""empleados = []
sueldos = []
totalsueldos = []
for x in range(3):
    nombre = str(input("Ingrese nombre\n"))
    empleados.append(nombre)
    su1 = int(input("Ingrese primer sueldo\n"))
    su2 = int(input("Ingrese segundo sueldo\n"))
    su3 = int(input("Ingrese tercer sueldo\n"))
    sueldos.append([su1,su2,su3])
for x in range(3):
    total = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    totalsueldos.append(total)
for x in range(3):
    print(empleados[x], totalsueldos[x])
posmayor = 0
mayor = totalsueldos[0]
for x in range(1,3):
    if totalsueldos[x] > mayor:
        mayor = totalsueldos[x]
        posmayor = x
print("Empleado con mayor sueldo en tres meses: ")
print(empleados[posmayor]) 
print("Con mayor ingreso: "+str(mayor))"""

lista = ["Irvin", "Karla", "Jose", "Fatima"]
print(lista)
lista.append("Carlos")
print(lista)
lista.pop(4)
print(lista)