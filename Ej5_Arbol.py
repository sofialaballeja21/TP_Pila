'''5.
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II.realizar un barrido ordenado alfabéticamente de cada árbol.'''

from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden,
    crear_bosque,
    contar_heroes_villanos,
    busqueda)

arbol = nodoArbol()
heroes = nodoArbol()
villanos = nodoArbol()

lista = [
    ['iron man', False, 1960],
    ['capiana marvel', False, 1890],
    ['thor', False, 1962],
    ['dotor strange', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
]
for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}

    insertar_nodo(arbol, nombre, datos)


#B
inorden(arbol)
print('-----------------------------')

#C
inorden_empieza_con(arbol, 'c')
print('-----------------------------')

#D
print('En el arbol hay: ',contar_heroes(arbol),'heroes')
print('-----------------------------')

#E
dato = busqueda(arbol, 'doctor strange')
if dato: 
    eliminar_nodo(arbol, 'doctor strange')
    modificado = input('Ingrese el nombre correcto: ')
    insertar_nodo(arbol, modificado)
postorden(arbol)
    
#F
postorden(arbol)
print('-----------------------------')
#G
print('bosque')
crear_bosque(arbol, heroes, villanos)
print('-----------------------------')

#G I
cantidad = {'villanos': 0, 'heroes': 0}
contar_heroes_villanos(arbol, cantidad)
print('cantidad de heroes y villanos', cantidad)
print('-----------------------------')

#G II
inorden(arbol)
print('arbol compleo')
print('-----------------------------')
print('heroes')
inorden(heroes)
print('-----------------------------')
print('villanos')
inorden(villanos)
print('-----------------------------')

print(eliminar_nodo(arbol, 'spider-man'))
print('-----------------------------')







