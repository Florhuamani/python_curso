#Programa que permita agregar nombre del producto, cantidad, precio unitario y total de pago, y mostrar el IGV y el total de pago en Python
nombre_producto:str=input("ingrese nombre del producto: ")
cantidad:str=int(input("ingrese cantidad del producto: "))
precioU:str=int(input("ingrese precio del producto: "))
total_pago:str=cantidad*precioU
IGV=total_pago*0.18
print("el IGV es: ",IGV,"el pago total es de S/.",total_pago)
precio_a_pagar=total_pago+IGV
print("precio facturizado:",precio_a_pagar)
#el IGV puede agregarse al costo, por ejemplo en plaza vea
#en otros casos te añaden el IGV dentro del precio


# Utilizando operadores de comparación, determina si un numero introducido por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10

#introducir numero
#str : porque mi variable tendra texto e input: porque dentro del texto existe numero
introduzca_numero:str=input("introduzca numero querido ususario: ")
#longitud es el numero de caracteres de un conjunto de numero y "len" nos permite obtener el numero de caracteres o la longitud de un dato introducido, pero este solo evalua "str" no "int"
longitud=len(introduzca_numero)
#ahora compararemos nuestro dato introducido con operadores de comparacion
comparando_longitud= longitud >= 3 and longitud <10
print(comparando_longitud)

