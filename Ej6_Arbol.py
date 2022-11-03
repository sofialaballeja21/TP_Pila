'''Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.'''


from arbol import (nodoArbol, insertar_nodo, 
                   inorden, por_nivel,
                   busqueda, inorden_JediMaster,
                   inorden_empieza_con, inorden_especies, 
                   postorden_ColorSable)
from lista import Lista

arbol_nombre = nodoArbol()
arbol_ranking = nodoArbol()
arbol_especie = nodoArbol()
arbol_color = nodoArbol()
lista = Lista()
 
lista = [['Leila Organa', 'human','11/08/133','blue', 'Jedi Knight', 'luke skywalker'],
         ['Lezra bridger', 'human','2/05/101', 'blue',  'Jedi Master','kanan jarrus'],
         ['anakin skywalker/darth vader', 'human','22/01/10', 'blue','Jedi Master', 'bobi-wan kenobi'],
         ['rey skywalker', 'human', '32/11/98', 'green','Padawan', 'yaddle'],
         ['oppo rancisis', 'thisspiasian', '2/05/101', 'green', 'Jedi Master', 'yaddle'],
         ['ahsoka tano', 'togruta', '22/55/800', 'yellow','Padawan','anakin skywalker'],
         ['asajj ventress', 'dathomirian','4/09/234', 'yellow', 'Jedi Knight',  'ky narec'],
         ['ki-adi-mundi', 'cerean','46/76/651', 'purple',  'Jedi Knight', '-']]


for nombre, especie, nacimiento, color_sable, ranking, maestro in lista:
    datos = {'Nombre': nombre, 'Especie': especie, 'Año de nacimiento': nacimiento, 'Color del sable de luz': color_sable, 'Ranking': ranking, 'Maestro': maestro}
    print(datos)
    #A
    insertar_nodo(arbol_nombre, nombre, datos)
    insertar_nodo(arbol_ranking, ranking, datos)
    insertar_nodo(arbol_especie, especie, datos)
    insertar_nodo(arbol_color, color_sable, datos)

#B 
print('°°°°°°°°°°°Inorden nombre°°°°°°°°°°°')
inorden(arbol_nombre)
print()
print('°°°°°°°°°°°Inorden ranking°°°°°°°°°°°')
inorden(arbol_ranking)
inorden(arbol_especie)

#C
print('°°°°°°°°°°°Barrido por nivel especie°°°°°°°°°°°')
por_nivel(arbol_especie)
print()
print('°°°°°°°°°°°Barrido por nivel especie°°°°°°°°°°°')
por_nivel(arbol_ranking)

#D
print('°°°°°°°°°°°Informacion de Luke Skywalker°°°°°°°°°°°')
busco = busqueda(arbol_nombre, 'ahsoka tano')
if busco:
    print('Datos: ', busco['datos'])

print()

#E    
print('°°°°°°°°°°°Informacion de Jedis Master°°°°°°°°°°°')
inorden_JediMaster(arbol_ranking)

print()

#F
print('°°°°°°°°°°°Sable de color green°°°°°°°°°°°')
color = postorden_ColorSable(arbol_color)
if color:
    lista.inserrtar(arbol_color['dato'])
    lista.barrido()

print()

#H
print('°°°°°°°°°°°Especies Togruta y Cerean°°°°°°°°°°°')
inorden_especies(arbol_especie)

print()

#I
print('°°°°°°°°°°°Empieza con la letra "L"°°°°°°°°°°°')
letra = inorden_empieza_con(arbol_nombre, 'L')
if letra:
    lista.insertar(arbol_nombre['dato'])
    lista.barrrido()










