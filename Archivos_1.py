def convierte_cadena(cadena):
    cadena_2=cadena.split('/n')
    cadena_vacia=[]
    for i in cadena_2:
        cadena_vacia.append(i.split(','))
    return cadena_vacia
def convierte_cadena_2(cadena_2):
    cadena_vacia=[]
    for i in cadena_2:
        clean=i.replace('/n','')
        valor=clean.split(',')
        cadena_vacia.append(valor)
    return cadena_vacia
def crear_diccionario(cadena):
    print(cadena)
    lista = convierte_cadena_2(cadena)
    diccionario = {}
    print('Esto es lista: ',lista)
    for i in range(1,len(lista)):
        # nombre = lista[0][i]
        # diccionario[nombre] = {
        #     "nombre":nombre,
        #     "edad": lista[1][i],
        #     "calificacion": lista[2][i]
        # }
    return diccionario

# Ejemplo de uso
#cadena = "Carlos,Mary,Luis/n10,20,30/n5,10,8"
Nombres=open("Nombres.txt","r")
lineas=Nombres.readlines()
diccionario = crear_diccionario(lineas)
print(diccionario)

# Para acceder a la información de cada persona
nombre = "Carlos"
if nombre in diccionario:
    print(f"{nombre} tiene {diccionario[nombre]['edad']} años y una calificación de {diccionario[nombre]['calificacion']}.")
else:
    print(f"No se encontró información para {nombre}.")



#CONVIERTE_CADENA
cadena='a,b,c/n10,15,20/n20,13,10/n20,13,/n'
# salida=convierte_cadena(cadena)
# print(salida)


#CONVIERTE_CADENA_2
#archivo_1=open(r"archivo.txt","r")
# lines=archivo_1.readlines()
# print(type(lines),lines)
# print(convierte_cadena_2(lines))
# archivo_1.close()



