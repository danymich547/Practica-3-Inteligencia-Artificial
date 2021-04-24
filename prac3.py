import pandas as pd
df=pd.DataFrame()
n=int(input("Ingrese cantidad a realizar proceso: "))

for i in range(n):
	i= i+1
	print ("Ingresar alumno \t")
	nombre= str(input("Nombre: "))	
	apellidos=str(input("Apellidos: "))
	edad = int(input("Edad: "))
	grado = str(input("Grado: "))	
	grupo = str(input("Grupo: "))		
	correo = str(input("Correo electronico: "))
	
	data = {'Nombre':[nombre], 'Apellidos':[apellidos], 'Edad':[edad], 'Grado':[grado], 'Grupo':[grupo],     			'Correo': 		        [correo]}
	
	g=int(input("Guardar datos y Salir \n 1.SI \n 2.NO "))
	df=df.append(data, ignore_index =True)
	
	if (g==1):
		df.to_csv("datosalumnos.csv")
	else:
		print("Hasta luego")
