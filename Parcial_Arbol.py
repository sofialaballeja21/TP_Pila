'''1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes de la saga de Star Wars, 
de los cuales se sabe su nombre, altura y peso. Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
e. mostrar un listado por nivel de los personajes del árbol;
f. determinar si Grogu esta en el árbol y responder lo siguiente:
mostrar toda su información;
en que tipo de nodo esta (hoja, intermedio o'''


from arbol import (nodoArbol, insertar_nodo, preorden, postorden,
                   inorden, busqueda, por_nivel, altura, modificar, eliminar_nodo,
                   inorden_personajes_altura, actualizar_altura, inorden_personajes_peso)

arbol = nodoArbol()
arbol_altura = nodoArbol()
arbol_peso = nodoArbol()


lista = [['Leila Organa', '0.2', '44kg'],
         ['Lezra bridger', '2,0', '70kg'],
         ['anakin skywalker', '1,60', '58kg'],
         ['rey skywalker', '3', '140kg'],
         ['oppo rancisis', '2,3', '90kg'],
         ['ahsoka tano', '0.5', '40kg'],
         ['asajj ventress', '1,50', '43kg'],
         ['ki-adi-mundi', '1,89', '87kg'],
         ['Luke Skywalker', '1,70', '74kg'],
         ['Darth Vader', '1,82', '76kg'],
         ['Yoda', '1,55', '49'],
         ['Boba Fett', '1,67', '60kg'],
         ['Kylo Ren', '2', '92kg'],
         ['Chewbacca', '3,4', '189kg'],
         ['Han Solo', '1,76', '80kg'],
         ['Obi-Wan Kenobi', '1,75', '70kg'],
         ['BB-8', '0.9', '80kg'],
         ['Mandalorian', '1,72', '70kg'],
         ['Grogu', '0.4', '23kg']]

for nombre, altura, peso in lista:
    datos = {'Nombre': nombre,
             'Altura': altura,
             'Peso': peso}

    insertar_nodo(arbol, nombre, datos)
    insertar_nodo(arbol_altura, altura, datos)
    insertar_nodo(arbol_peso, peso, datos)

#inorden(arbol)

#A se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
nuevo_nombre = input('Ingrese el nombre: ')
insertar_nodo(arbol, nuevo_nombre, datos)
nuevo_peso = input('Ingrese el peso: ')
insertar_nodo(arbol_peso,nuevo_peso, datos)
nuevo_altura = input('Ingrese la altura: ')
insertar_nodo(arbol_altura, nuevo_altura, datos)
print()
inorden(arbol)
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

modif = input('A quien quiere modificar? ')
pesonaje = busqueda(arbol, modif)
if pesonaje:
    eliminar_nodo(arbol, modif)
    modificacion = modificar(arbol, campo = nombre) 
    if modificacion:   
        modificacion = input('Ingrese el nombre modificado')
        insertar_nodo(arbol, modificacion)
    postorden(arbol)


baja = input('Personaje que va adar de baja: ')
eliminar_nodo(arbol, baja)
print('Personaje eliminado: ', baja)
print()


#B mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
'''buscar = busqueda(arbol, 'Yoda')
if buscar:
    print('Informacion: ', buscar['datos'])
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

buscar = busqueda(arbol, 'Mandalorian')
if buscar:
    print('Informacion: ', buscar['datos'])
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

buscar = busqueda(arbol, 'Luke Skywalker')
if buscar:
    print('Informacion: ', buscar['datos'])
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')'''


#C  mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
'''inorden_personajes_altura(arbol_altura)
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print()
#D mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
inorden_personajes_peso(arbol_peso)
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print()
#E mostrar un listado por nivel de los personajes del árbol;
por_nivel(arbol)
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print()'''

#F determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o aíz);
# que altura tiene el nodo dentro del árbol.

'''buscar = busqueda(arbol, 'Grogu')
if buscar:
    print('Informacion: ', buscar['datos'])
    print(altura(arbol))
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print()'''
























