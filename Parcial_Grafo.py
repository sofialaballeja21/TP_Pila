'''2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
a. cada vértice debe almacenar el nombre de un personaje, 
las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,  Boba Fett, Leia, Rey, 
Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.
'''
from grafo import Grafo
from grafo import Arista
grafo = Grafo(dirigido=False)
arista = Arista()

#D
grafo.insertar_vertice('Luke Skywalker')
grafo.insertar_vertice('Darth Vader')
grafo.insertar_vertice('Yoda') 
grafo.insertar_vertice('Boba Fett')
grafo.insertar_vertice('Leila')
grafo.insertar_vertice('ahsoka tano') 
grafo.insertar_vertice('Rey')
grafo.insertar_vertice('Kylo Ren')
grafo.insertar_vertice('Chewbacca')
grafo.insertar_vertice('Han Solo')
grafo.insertar_vertice('R2-D2')
grafo.insertar_vertice('Obi-Wan Kenobi')
grafo.insertar_vertice('BB-8')


grafo.insertar_arista('Luke Skywalker', 'Darth Vader', 4)
grafo.insertar_arista('Luke Skywalker', 'Leia', 300)
grafo.insertar_arista('Darth Vader', 'R2-D2', 5)
grafo.insertar_arista('Darth Vader', 'BB-8', 453)
grafo.insertar_arista('Yoda', 'Han Solo', 12)
grafo.insertar_arista('Yoda', 'ahsoka tano', 198)
grafo.insertar_arista('Boba Fett', 'Leia', 42)
grafo.insertar_arista('Boba Fett', 'BB-8', 34)
grafo.insertar_arista('Leila', 'Han Solo', 442)
grafo.insertar_arista('Leila', 'Obi-Wan Kenobi', 100)
grafo.insertar_arista('ahsoka tano', 'Boba Fett', 127)
grafo.insertar_arista('ahsoka tano', 'Han Solo', 742)
grafo.insertar_arista('Rey', 'Kylo Ren', 563)
grafo.insertar_arista('Rey', 'Obi-Wan Kenobi', 632)
grafo.insertar_arista('Kylo Ren', 'BB-8', 132)
grafo.insertar_arista('Kylo Ren', 'Leila', 442)
grafo.insertar_arista('Chewbacca', 'R2-D2', 45)
grafo.insertar_arista('Chewbacca', 'Yoda', 87)
grafo.insertar_arista('Han Solo', 'Obi-Wan Kenobi', 72)
grafo.insertar_arista('Han Solo', 'Darth Vader', 84)
grafo.insertar_arista('R2-D2', 'Boba Fett', 442)
grafo.insertar_arista('R2-D2', 'ahsoka tano', 100)
grafo.insertar_arista('Obi-Wan Kenobi','Kylo Ren', 53)
grafo.insertar_arista('Obi-Wan Kenobi', 'R2-D2', 13)
grafo.insertar_arista('BB-8', 'Yoda', 354)
grafo.insertar_arista('BB-8', 'ahsoka tano', 232)

'''b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;'''

arbol = grafo.kruskal()
     #print(arbol_min)
arbol = arbol[0].split('-')
peso_total = 0
for nodo in arbol:
     nodo = nodo.split(';')
     #print(nodo)
     peso_total += int(nodo[2])
     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print(f"Arbol de expancion minimo: {peso_total}")

 
#c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);



#e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.
























