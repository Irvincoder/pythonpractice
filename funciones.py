"""def Bienvenida():
    print("Este es un mensaje de bienvenida")
def Suma():
    num1 = int(input("Ingrese primer valor\n"))
    num2 = int(input("Ingrese segundo valor\n"))
    total = num1 + num2
    print("El total de la suma es: "+str(total))
def Final():
    print("Gracias por usar el programa")    
Bienvenida()
Suma()
Final()"""

"""def Suma():
    num1 = int(input("Ingrese primer valor\n"))
    num2 = int(input("Ingrese segundo valor\n"))
    total = num1 + num2
    print(total)
def separacion():
    print("/*********************/")
for x in range(5):
    Suma()
    separacion()"""

"""def Notas():
    name = str(input("Ingrese nombre del alumno\n"))
    nota1 = int(input("Ingrese primera nota\n"))
    nota2 = int(input("Ingrese segunda nota\n"))
    nota3 = int(input("Ingrese tercera nota\n"))
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    print("Nombre del alumno: " +name+" Pormedio de notas: "+str(promedio))
def Separacion():
    print("/*******************/")
for x in range(3):
    Notas()
    Separacion()"""

"""def Mensaje(mensaje):
    print("/*************/")
    print(mensaje)
    print("/*************/")
Mensaje("Hola como estas")"""

"""def notas(n1,n2,n3):
    suma = n1 + n2 + n3
    promedio = suma / 3
    print(promedio)
notas(10,10,10)"""

"""def Mayor(v1,v2,v3):
    print("El valor mayor de los tres es:")
    if v1 > v2 and v1 > v3:
        print(v1)
    else:
        if v2 > v3:
            print(v2)
        else:
            print(v3)
def cargar():
    valor1 = int(input('Ingrese valor 1 \n'))
    valor2 = int(input('Ingrese valor 2 \n'))
    valor3 = int(input('Ingrese valor 3 \n'))
    Mayor(valor1, valor2, valor3)
cargar()"""

"""def notas(n1,n2,n3):
    print("Promedio de notas")
    suma = n1 + n2 + n3
    promedio = suma / 3
    if promedio > 7:
        print("Pasastes: "+str(promedio))
    else:
        print("No pasastes: "+str(promedio))
def Cargar():
    nota1 = int(input("Ingrese primera nota\n"))
    nota2 = int(input("Ingrese segunda nota\n"))
    nota3 = int(input("Ingrese tercera nota\n"))
    notas(nota1,nota2,nota3)
Cargar()"""

"""def Superficie(lado):
    sup = lado * lado
    return sup
valor = int(input("Ingrese valor\n"))
superficie = Superficie(valor)
print("La superficie es: "+str(superficie))"""

"""def retonar_mayor(v1,v2):
    if v1 > v2:
        mayor = v1
    else:
        mayor = v2
    return mayor
valor1 = int(input("Ingrese valor uno\n"))
valor2 = int(input("Ingrese valor dos\n"))
print(retonar_mayor(valor1,valor2))"""

"""def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma
def mayor(lista):
    may = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may
def menor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men
listavalores = [10, 25, 250, 30, 50]
print("lista completa: "+str(listavalores))
print("lista sumarizada: "+str(sumarizar(listavalores)))
print("lista mayor: "+str(mayor(listavalores)))
print("lista menor: "+str(menor(listavalores)))"""

"""def mayormenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        else:
            if lista[x] < menor:
                menor = lista[x]
    print("El valor mayor es: "+str(mayor))
    print("El valor menor es: "+str(menor))
#bloque principal
lista = []
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    lista.append(valor)
mayormenor(lista)"""

"""def cargar_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese valor\n"))
        li.append(valor)
    return li
def imprimir_mayor10(li):
    print("Valores mayores a 10")
    for x in range(len(li)):
        if li[x] > 10:
            print(li[x])
lista = cargar_lista()
imprimir_mayor10(lista)"""

"""def cargar_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese valor\n"))
        li.append(valor)
    return li
def mayormenor(li):
    mayor = li[0]
    menor = li[0]
    for x in range(1, len(li)):
        if li[x] > mayor:
            mayor = li[x]
        else:
            if li[x] < menor:
                menor = li[x]
    return [mayor, menor]
lista = cargar_lista()
rango = mayormenor(lista)
print("Mayor de la lista: "+str(rango[0]))
print("Menor de la lista: "+str(rango[1]))"""

"""def datos():
    nombre = []
    edad = []
    for x in range(3):
        nom = str(input("Ingrese nombre\n"))
        nombre.append(nom)
        eda = int(input("Ingrese edad\n"))
        edad.append(eda)
    return [nombre, edad]
def mayor(nombre,edad):
    print("nombres de personas mayores")
    for x in range(len(nombre)):
        if edad[x] >= 18:
            print(nombre[x])
def promedio(edad):
    suma = 0 
    for x in range(len(edad)):
        suma = suma + edad[x]
    promedio = suma // 5
    print("promedio de edad: "+str(promedio))
nombres, edades = datos()
mayor(nombres,edades)
promedio(edades)"""

"""def calcular_sueldos(nombre, costohora, cantidadhoras):
    sueldo = costohora * cantidadhoras
    print(nombre, "trabajo", cantidadhoras, "y cobra un suledo de ", sueldo)
calcular_sueldos("Juan", 10, 20)
calcular_sueldos(costohora=20, cantidadhoras=80, nombre="ana")
calcular_sueldos(costohora=5, cantidadhoras=10, nombre="karla")"""

"""def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingresea valor\n"))
        lista.append(valor)
    return lista
def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")
li = cargar()
imprimir(li)"""

"""def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma
def mayor(lista):
    may = lista[0]
    for x in range(1,len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may
def menor(lista):
    men = lista[0]
    for x in range(1,len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men
#Bloque principal#
listavalores = [10, 25, 50, 35, 100]
print("Lista completa: "+str(listavalores))
print("Suma de los valores de la lista: "+str(sumarizar(listavalores)))
print("El mayor de la lista: "+str(mayor(listavalores)))
print("El menor de la lista: "+str(menor(listavalores)))"""

"""def mayor_menor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        else:
            if lista[x] < men:
                men = lista[x]
    print("El valor mayor es: "+str(may))
    print("El valor menor es: "+str(men))
#bloque
lista = []
for x in range(5):
    valor = int(input("Ingrese valor\n"))
    lista.append(valor)
mayor_menor(lista)"""

"""def cargar_lista():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese valor\n"))
        lista.append(valor)
    return lista
def imprimirMayor(lista):
    print("Numeros mayores a 10:")
    for x in range(len(lista)):
        if lista[x] > 10:
            print(lista[x])
lista = cargar_lista()
imprimirMayor(lista)"""

"""def cargar():
    lista = []
    for x in range(5):
        n = int(input("Ingrese valor\n"))
        lista.append(n)
    return lista
def mayormenor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        else:
            if lista[x] < men:
                men = lista[x]
    return [may , men]
lista = cargar()
rango = mayormenor(lista)
print("El mayor de la lista es: "+str(rango[0]))
print("El menor de la lista es: "+str(rango[1]))"""

"""def Datos():
    nom = []
    eda = []
    for x in range(5):
        nombre = str(input("Ingrese nombre\n"))
        nom.append(nombre)
        edades = int(input("Ingrese edad\n"))
        eda.append(edades)
    return [nom, eda]
def mayores_edad(nom,eda):
    for x in range(len(nom)):
        if eda[x] >= 18:
            print(nom[x])
def promedio(eda):
    suma = 0
    for x in range(len(eda)):
        suma = suma + eda[x]
    promedio = suma // 5
    print("El promedio de edad es: "+str(promedio))
nombres, edades = Datos()
mayores_edad(nombres, edades)
promedio(edades)"""

"""def Notas():
    lista = []
    for x in range(3):
        n = int(input("Ingrese nota\n"))
        lista.append(n)
    return lista
def mayor_nota(lista):
    for x in range(len(lista)):
        if lista[x] >= 7:
            print(lista[x])
#bloque pricipal
lista = Notas()
mayor_nota(lista)"""

"""def Notas():
    notas = []
    for x in range(5):
        nota = int(input("Ingrese nota\n"))
        notas.append(nota)
    return notas
def mayor_menor(notas):
    mayor = notas[0]
    menor = notas[0]
    for x in range(5):
        if notas[x] > mayor:
            mayor = notas[x]
        else:
            if notas[x] < menor:
                menor = notas[x]
    return [mayor, menor]
#bloque principal
notas = Notas()
rango = mayor_menor(notas)
print("La nota mayor es: "+str(rango[0]))
print("La nota menor es: "+str(rango[1]))"""

"""def Datos():
    nombres = []
    notas = []
    for x in range(5):
        nombre = str(input("Ingrese nombre\n"))
        nombres.append(nombre)
        nota = int(input("Ingrese nota\n"))
        notas.append(nota)
    return [nombres, notas]
def Notas_Mayores(nombres, notas):
    print("Nombres con notas mayores")
    for x in range(5):
        if notas[x] >= 7:
            print(nombres[x])
def Promedio_Notas(notas):
    suma = 0
    for x in range(5):
        suma = suma + notas[x]
    promedio = suma // 5
    print("El promedio de todas las notas es: "+str(promedio))
#bloque principal
nombres, notas = Datos()
Notas_Mayores(nombres, notas)
Promedio_Notas(notas)"""

"""def Notas(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        else:
            if lista[x] < men:
                men = lista[x]
    print("La nota mayor es: "+str(may))
    print("La nota menor es: "+str(men))
#bloque princial
lista = []
for x in range(5):
    n = int(input("Ingrese nota\n"))
    lista.append(n)
Notas(lista)"""

"""def titulo(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))
#bloque principal
titulo("Hola soy irvin")
titulo("web","-")"""

'''def calcular_sueldo(nombre,costohora,cantidadhora):
    sueldo = costohora *cantidadhora
    print(nombre, "trabajo", cantidadhora, "y cobra un sueldo", sueldo)
#bloque principal
calcular_sueldo("juan",5,44)
calcular_sueldo(nombre="karla",costohora=8, cantidadhora=60)
calcular_sueldo(cantidadhora=100, costohora=10,nombre="Irvin")'''

def suma(v1,v2,*lista):
    suma = v1 + v2
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma
#bloque principal
print("La suma 1 + 2")
print(suma(1,2))
print("La suma de 1 + 2 + 3 + 4")
print(suma(1,2,3,4))
print("La suma de 1 + 2 + 3 +4 + 5 + 6")
print(suma(1,2,3,4,5,6))