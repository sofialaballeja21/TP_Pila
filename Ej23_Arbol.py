from arbol import (busqueda, eliminar_nodo, inorden_heracles, 
                   inorden_no_derrotadas, insertar_nodo, mayor_derrota, nodoArbol, 
                   inorden, por_nivel, inorden_heracles, modificar)
from lista import Lista

arbol = nodoArbol()
lista_derrotados = Lista()
heroesdioses = nodoArbol()
derrotados = nodoArbol()

lista = [['Ceto', '-'], 
         ['Cerda de Cromion', 'Teseo'],
         ['Tifon', 'Zeus'], 
         ['Heracles', 'Ortro'],
         ['Equidna', 'Argos Panoptes'], 
         ['Toro de Creta', 'Teseo'],
         ['Dino', '-'], 
         ['Jabali de Calidon','Atlanta'],
         ['Pefredo', '-'], 
         ['Carcinos', '-'],
         ['Enio', '-'], 
         ['Heracles','Gerion'],
         ['Escila', '-'], 
         ['Cloto', '-'],
         ['Caribdis', '-'], 
         ['Laquesis', '-'],
         ['Euriale','-'], 
         ['Atropos', '-'],
         ['Esteno', '-'],
         ['Minotaurod de Creta', 'Teseo'],
         ['Medusa','Perseo'], 
         ['Harpias', '-'],
         ['Heracles', 'Ladon'],
         ['Argos Panoptes', 'Hermes'],
         ['Qimera', 'Belerofonte'], 
         ['Talos', 'Medea'],
         ['Heracles', 'Hidra de Lerna'], 
         ['Sirenas', '-'],
         ['Heracles', 'Leon de Nemea'], 
         ['Piton', 'Apolo'],
         ['Esfinge', 'Edipo'], 
         ['Cierva de Cerinea', '-'],
         ['Dragon de Colquida', '-'], 
         ['Basilisco', '-'],
         ['Cerbero', '-'], 
         ['Jabali de Erimanto', '-'],
         ['Aves del Estínfalo', '-']
]

NuevoCampo = {}

for criatura, derrotado in lista:
    #B
    descripcion = input(f'Ingrese una breve descripcion de {criatura}: ')
    #G
    captura = input(f'Ingrese quien campturo al personaje {criatura}: ')
    datos = {'nombre de la criatura': criatura, 'derroto a': derrotado,'descripcion': descripcion, 'capturo': captura}
    print(datos)
    insertar_nodo(arbol, criatura, derrotado)
    
print()


#A
print('***********Barrido inorden***********')
inorden(arbol)
print()

#C
print('***********Informacion de Talos***********')
busq = busqueda(arbol, 'Talos')
if busq:
    print('Informacion: ', busq['datos'])
print('-------------------------------------')

#D, #d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;


#E
print('***********Criaturas que derroto Heracles***********')
inorden_heracles(arbol)

#F
print('***********Criaturas no derrotadas***********')
inorden_no_derrotadas(arbol)

#H,#h. modifique los nodos de las criaturas Cerbero, 
# Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;


cerbero = busqueda(arbol, 'Aves del Estinfalo')
if cerbero:
    modificacion = modificar(arbol, campo = captura) 
    if modificacion:   
        cerbero_modificacion = 'jose'
        insertar_nodo(arbol, cerbero_modificacion)
    
print(datos)


#I, #i. se debe permitir búsquedas por coincidencia;


#J
eliminar_basilico = eliminar_nodo(arbol, 'Basilisco')
print('Personaje eliminado: ', eliminar_basilico)
print()

eliminar_sirenas = eliminar_nodo(arbol, 'Sirenas')
print('Personaje eliminado: ', eliminar_sirenas)
print('-------------------------------------')
    
    
#K
aves = busqueda(arbol, 'Aves del Estinfalo')
if aves:
    eliminar_nodo(arbol, '-')
    aves_modificado = input('Ingrese el nombre correcto')
    insertar_nodo(arbol, aves_modificado)
    
#L
ladon = busqueda(arbol, 'Heracles') #ingreso por el campo criatura
if ladon: 
    eliminar_nodo(arbol, 'Ladon') #elimino el nodo donde se almacena Ladon
    ladon_modificado = input('Ingrese el nombre correcto: ')
    insertar_nodo(arbol, ladon_modificado)
inorden(arbol)


#M
print('***********Listado por nivel***********')
por_nivel(arbol) 
print('-------------------------------------')

#N, #n. muestre las criaturas capturadas por Heracles. 
    
    
