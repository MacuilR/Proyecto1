from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

import os
import time

os.system ("clear")

print('\t\t\tBIENVENIDO AL DEPARTAMENTO ELÉCTRONICO DE BT21\nPor favor ingresa tu usuario y contraseña')

# Lista de administradores, son los únicos con el poder de acceder a  información de ventas.

admin = [['Alberto1020', '030920lop'],['LorenaD1702','020920lin'],['CynthiaG2109','len182330']]

#Se le pide al usuario sus datos
usuario = input("Usuario: ")
contrasenia = input("Contraseña: ")

text_bienvenida = print('\t\t\t\t¡Hola administrador!\n\nIngrese a la información actualizada que desea conocer')

#Las condiciones para que el usuario pueda ingresar
if usuario == admin[0][0] and contrasenia == admin[0][1]:
	print(text_bienvenida)

elif usuario == admin[1][0] and contrasenia == admin[1][1]:
	print(text_bienvenida)

elif usuario == admin[2][0] and contrasenia == admin [2][1]:
	print(text_bienvenida)
else:
	print('Lo sentimos, usted no está autorizado para ingresar a este sistema')

os.system ("clear")

#Una vez que el usuario comprobó ser administrador se muestra el menú
print('\t\t MENÚ\n A. Ventas de productos e intereses de los clientes\n B. Reseñas en servicio \n C. Ingresos por ventas\n\nEscriba A, B o C según le interese')
print('\nPara consultar otra categoría del menú deberá volver a introducir sus datos.\n')

seleccion = input('-> ')
time.sleep(5)
os.system ("clear")

if seleccion == 'A':

	print('\t\tTOP 50 DE PRODUCTOS MÁS VENDIDOS\n')
	ventas = [producto[1] for producto in lifestore_sales] #Id de los productos vendidos.
	v_acum = [[ventas.count(frec), frec ] for frec in set(ventas)] #frecuencia por producto
	
	v_acum.sort(reverse = True)
	top_50 = v_acum[0:49] 
	print('Se presentan los 50 productos con mayores ventas, [frecuencia de ventas, id del producto]:\n\n', top_50)

	top_10 = v_acum[0:9]
	print('El Top 10 de los productos más vendidos es: \n\n', top_10)

	v_acum.sort()
	menores_ventas = v_acum[0:27]
	print('Los productos con menores ventas son: \n\n', menores_ventas)

	ids_lp = [elemento[0] for elemento in lifestore_products]
	ids_ls = [elemento[1] for elemento in lifestore_sales]
	sin_v = [[ids_ls.count(frec), frec] for frec in set(ids_lp)]
	sin_v.sort()
	no_ventas = sin_v[0:54]
	print('Los productos sin ventas en el período de estudio segun [frecuencia de productos en ventas, id]: \n\n', no_ventas)

	print('\n\t\tTOP EN BÚSQUEDAS\n')

	busqueda = [producto[1] for producto in lifestore_searches]
	num_b = [[busqueda.count(frec),frec] for frec in set(busqueda)] #Se presenta el id de los productos y su frecuencia de búsqueda

	num_b.sort(reverse = True)
	top_50_busq = num_b[0:49]
	print('Se presentan los 50 productos que más buscan los clientes, [frecuencia de busqueda, id producto]:\n\n', top_50_busq)

	top_10_busq = num_b[0:10]
	print('Top 10 de productos más buscados, [frecuencia de busqueda, id producto: \n\n', top_10_busq)

	print('\n\t\tLOS MENOS BUSCADOS\n')
	num_b.sort()
	menores_b = num_b[0:29]
	print('Los productos menos buscados son, [frecuencia de busqueda, id producto]: \n\n', menores_b)

	print('\n\t\tLOS QUE NADIE BUSCÓ\n')
	ids_lp = [elemento[0] for elemento in lifestore_products]
	ids_lse = [elemento[1] for elemento in lifestore_searches]
	sin_busq = [[ids_lse.count(frec), frec] for frec in set(ids_lp)]
	sin_busq.sort()
	no_busq = sin_busq[0:40]
	print('Los productos sin ventas en el período de estudio son, [frecuencia de busqueda, id]:\n\n', no_busq)

	print('\n\t\tPRODUCTOS POR CATEGORÍA\n')
	categoria_lp = [elemento[3] for elemento in lifestore_products]
	num_prod_cat = [[categoria_lp.count(frec), frec] for frec in set(categoria_lp)]
	num_prod_cat.sort(reverse = True)
	orden_cat = num_prod_cat[0:8]
	print('Categorías ordenadas según el número de productos de cada una de ellas: \n', orden_cat)

	print('\n\t\tVENTAS POR CATEGORÍA\n')
	id_categ = [[elemento[0], elemento[3]] for elemento in lifestore_products] #lista con [id,categoria]

	print('Dentro del top 50 de ventas se muestran las categorías de productos a las que pertenecen.Se presentan como: [id, frecuencia de venta, categoria] \n')

	for id in top_50:
		for c in id_categ:
			if id[1] == c[0]:
				categ_top50 = [id[1], id[0],c[1]]
				print(categ_top50)

	print('Dentro de los productos sin ventas se muestran las categorías a las que pertenecen. Se presentan como: [id, frecuencia de venta, categoria]\n')
	for id in no_ventas:
		for c in id_categ:
			if id[1] == c[0]:
				categ_NoVentas = [id[1],id[0],c[1]]
				print(categ_NoVentas)


elif seleccion == 'B':

	print('\t\t RESEÑAS\n')
	print('\t\t MEJORES RESEÑAS\n')

	id_ScoreDev = [[el[1], el[2], el[4]] for el in lifestore_sales]

	print('Los productos con reseñas de 5 estrellas y sin devoluciones son:\n')

	for score in id_ScoreDev:
		if score[1] == 5:
			score5 = [score[0], score[1], score[2]]
			print(score5)

	print('Los productos con reseñas de 4 estrellas y sin devoluciones son: \n')
	for score in id_ScoreDev:
		if score[1] == 4:
			score4 = [score[0], score[1], score[2]]
			print(score4)    


	print('Los productos con reseñas de 3 estrellas y sin devoluciones son: \n')
	for score in id_ScoreDev:
		if score[1] == 3 and score[2] == 0:
			score3 = [score[0], score[1], score[2]]
			print(score3)  

	print('\t\t PEORES RESEÑAS\n')

	print('Los productos con reseñas de 1 estrella son: \n')
	for score in id_ScoreDev:
		if score[1] == 1:
			score1 = [score[0], score[1], score[2]]
			print(score1) 

	print('Los productos con devoluciones son: \n')
	for dev in id_ScoreDev:
		if dev[2] == 1:
			devolucion = [dev[0], dev[1], dev[2]]
			print(devolucion)


elif seleccion == 'C':

	print('\t\tINGRESOS POR VENTAS\n')

	ventas = [producto[1] for producto in lifestore_sales]  
	v_acum = [[ventas.count(frec), frec ] for frec in set(ventas)]
    
	for producto in v_acum:
		for precio in lifestore_products:
			if producto[1] == precio[0]:
				ventas_inc = [producto[0],producto[1],precio[2]]  

	ingreso_v = 0

	for id in lifestore_sales:
	  for precio in lifestore_products:
	    if id[1] == precio[0]:
	      ingreso_v += precio[2]

	ingreso_promM = ingreso_v / 12 # Las ventas mensuales promedio    
 
	print('El ingreso por ventas durante 2020 fue de:\t$', ingreso_v, '\nEl valor promedio por ventas mensuales es de:\t', round(ingreso_promM,2))

	print('\n\t\tINGRESOS MENSUALES POR VENTAS\n')

	fecha_v = [[el[3], el[1]] for el in lifestore_sales]
	mes = slice(3,5,1)

	## ENERO
	enero = '01'
	producto_v1 = 0
	ingreso_v1 = 0

	for elemento in fecha_v:
		if enero == elemento[0][mes]:
			producto_v1 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v1 += precio[2]

	ingreso_vpm1 = ingreso_v1 / 30

	print('\n\tENERO\n\nLas ventas durante el mes de enero fueron de: \t$',ingreso_v1, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm1,2))

	### FEBRERO 
	febrero = '02'
	producto_v2 = 0
	ingreso_v2 = 0

	for elemento in fecha_v:
		if febrero == elemento[0][mes]:
			producto_v2 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v2 += precio[2]

	ingreso_vpm2 = ingreso_v2 / 30

	print('\n\tFEBRERO\n\nLas ventas durante el mes de febrero fueron de: \t$',ingreso_v2, '\nLas ventas promedio por día ascienden a: \t$', ingreso_vpm2)

	### MARZO
	marzo = '03'
	producto_v3 = 0
	ingreso_v3 = 0

	for elemento in fecha_v:
		if marzo == elemento[0][mes]:
			producto_v3 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v3 += precio[2]

	ingreso_vpm3 = ingreso_v3 / 30

	print('\n\tMARZO\n\nLas ventas durante el mes de marzo fueron de: \t$',ingreso_v3, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm3,2))

	### ABRIL
	abril = '04'
	producto_v4 = 0
	ingreso_v4 = 0

	for elemento in fecha_v:
		if abril == elemento[0][mes]:
			producto_v4 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v4 += precio[2]

	ingreso_vpm4 = ingreso_v4 / 30

	print('\n\tABRIL\n\nLas ventas durante el mes de abril fueron de: \t$',ingreso_v4, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm4,2))

	### MAYO
	mayo = '05'
	producto_v5 = 0
	ingreso_v5 = 0

	for elemento in fecha_v:
		if mayo == elemento[0][mes]:
			producto_v5 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v5 += precio[2]

	ingreso_vpm5 = ingreso_v5 / 30

	print('\n\tMAYO\n\nLas ventas durante el mes de mayo fueron de: \t$',ingreso_v5, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm5,2))

	### JUNIO
	junio = '06'
	producto_v6 = 0
	ingreso_v6 = 0

	for elemento in fecha_v:
		if junio == elemento[0][mes]:
			producto_v6 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v6 += precio[2]

	ingreso_vpm6 = ingreso_v6 / 30

	print('\n\tJUNIO\n\nLas ventas durante el mes de junio fueron de: \t$',ingreso_v6, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm6,2))

	### JULIO
	julio = '07'
	producto_v7 = 0
	ingreso_v7 = 0

	for elemento in fecha_v:
		if julio == elemento[0][mes]:
			producto_v7 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v7 += precio[2]

	ingreso_vpm7 = ingreso_v7 / 30

	print('\n\tJULIO\n\nLas ventas durante el mes de julio fueron de: \t$',ingreso_v7, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm7,2))

	### AGOSTO
	agosto = '08'
	producto_v8 = 0
	ingreso_v8 = 0

	for elemento in fecha_v:
		if agosto == elemento[0][mes]:
			producto_v8 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v8 += precio[2]

	ingreso_vpm8 = ingreso_v8 / 30

	print('\n\tAGOSTO\n\nLas ventas durante el mes de agosto fueron de: \t$',ingreso_v8, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm8,2))

	### SEPTIEMBRE
	septiembre = '09'
	producto_v9 = 0
	ingreso_v9 = 0

	for elemento in fecha_v:
		if septiembre == elemento[0][mes]:
			producto_v9 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v9 += precio[2]

	ingreso_vpm9 = ingreso_v9 / 30

	print('\n\tSEPTIEMBRE\n\nLas ventas durante el mes de septiembre fueron de: \t$',ingreso_v9, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm9,2))

	### OCTUBRE
	octubre = '10'
	producto_v10 = 0
	ingreso_v10 = 0

	for elemento in fecha_v:
		if octubre == elemento[0][mes]:
			producto_v10 += 1
			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v10 += precio[2]

	ingreso_vpm10 = ingreso_v10 / 30

	print('\n\tOCTUBRE\n\nLas ventas durante el mes de octubre fueron de: \t$',ingreso_v10, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm10,2))

	### NOVIEMBRE
	noviembre = '11'
	producto_v11 = 0
	ingreso_v11 = 0

	for elemento in fecha_v:
		if noviembre == elemento[0][mes]:
			producto_v11 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v11 += precio[2]

	ingreso_vpm11 = ingreso_v11 / 30

	print('\n\tNOVIEMBRE\n\nLas ventas durante el mes de noviembre fueron de: \t$',ingreso_v11, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm11,2))

	### DICIEMBRE
	diciembre = '12'
	producto_v12 = 0
	ingreso_v12 = 0

	for elemento in fecha_v:
		if diciembre == elemento[0][mes]:
			producto_v12 += 1

			for precio in lifestore_products:
				if elemento[1] == precio[0]:
					ingreso_v12 += precio[2]

	ingreso_vpm12 = ingreso_v12 / 30

	print('\n\tDICIEMBRE\n\nLas ventas durante el mes de diciembre fueron de: \t$',ingreso_v12, '\nLas ventas promedio por día ascienden a: \t$', round(ingreso_vpm12,2))

	# MES CON MAYORES VENTAS

	lista_final = [ingreso_v1, ingreso_v2, ingreso_v3, ingreso_v5, ingreso_v6, ingreso_v7, ingreso_v8, ingreso_v9, ingreso_v10, ingreso_v11, ingreso_v11]
	lista_final.sort(reverse = True)

	print('\n\n\t\t\tTOP 3 DE MAYORES VENTAS\n\t\t\t\t1. Marzo\n\t\t\t\t2. Enero\n\t\t\t\t3. Febrero')

	print('\n\n\t\t\t\tSIN VENTAS\n\t\t\tOtubre y Diciembre')


else:
	print('Esa opción no está disponible')

