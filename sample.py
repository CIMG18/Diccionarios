lista=[['nombre','edad','calificacion','apellido'],['carlos',14,9,'martinez'],['maria',14,9,'martinez'],['juan',14,9,'martinez']]

labels = lista[0]
salida= []
for i in range(1,len(lista)):
    item = lista[i]
    # [('c', 3), ('d', 4), ('a', 1), ('b', 2)] Pareja Llave,Valor en tupla
    values = [(labels[i],item[i]) for i in range(len(labels))]
    print("values", values)
    # dicci['nombre']=carlos
    diccio = {key:value for (key,value) in values} #Diccionario de comprension
    print("diccio", diccio)
    salida.append(diccio)