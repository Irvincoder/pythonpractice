"""mi_tupla = ("Irvin")
mi_tupla2 = (1,2,3)
mi_tupla3 = (0.5,2.5)
mi_tupla4 = (True)
print(mi_tupla)
print(mi_tupla2)
print(mi_tupla3)
print(mi_tupla4)"""

"""def carga_fecha():
	dd = int(input("Ingrese dia\n"))
	mm = int(input("Ingrese mes\n"))
	yy = int(input("Ingrese año\n"))
	return (dd,mm,yy)
def imprimir_fecha(fecha):
	print(fecha[0],fecha[1],fecha[2],sep="/")
#bloque principal
fecha = carga_fecha()
imprimir_fecha(fecha)"""

'''fechatupla = (10, 7,2021)
print("Primera tupla")
print(fechatupla)
fechalista = list(fechatupla)
print("Tupla convertida en lista")
print(fechalista)
fechalista[0] = 11
print("Lista modificada")
print(fechalista)
fechalistamo = tuple(fechalista)
print("Lista convertida a tupla")
print(fechalistamo)'''

'''empleado = ["Irvin", 32, (6, 6, 1989)]
print(empleado)
empleado.append((10,6,1989))
print(empleado)
alumno = ("Pedro", 15, [10,5])
print(alumno)
alumno[2].append(10)
print(alumno)'''

def paises():
	paises = []
	for x in range(2):
		nom = str(input("Ingrese nombre pais\n"))
		can = int(input("Ingrese cantidad de habitantes\n"))
		paises.append((nom,can))
	return paises
def imprimir(paises):
	for x in range(len(paises)):
		print(paises[x][0],paises[x][1])
def mayor_habitantes(paises):
	pos = 0
	for x in range(1, len(paises)):
		if paises[x][1] > paises[pos][1]:
			pos = x
	print("pais con mayor cantidad de habitantes es: "+str(paises[pos][0]))
#bloque principal
paises = paises()
imprimir(paises)
mayor_habitantes(paises)			