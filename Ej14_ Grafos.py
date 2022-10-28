'''14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:
a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.'''

from grafo import Grafo


grafo = Grafo(dirigido=False)

grafo.insertar_vertice('Cocina')
grafo.insertar_vertice('Comedor')
grafo.insertar_vertice('Cochera')
grafo.insertar_vertice('Quincho')
grafo.insertar_vertice('Baño 1')
grafo.insertar_vertice('Baño 2')
grafo.insertar_vertice('Habitacion 1')
grafo.insertar_vertice('Habitacion 2')
grafo.insertar_vertice('Sala de estar')
grafo.insertar_vertice('Terraza')
grafo.insertar_vertice('Patio')


grafo.insertar_arista('Cocina', 'Comedor', 10)
grafo.insertar_arista('Cocina', 'Patio', 30)
grafo.insertar_arista('Cocina', 'Baño 1', 15)
grafo.insertar_arista('Comedor', 'Habitacion 1', 12)
grafo.insertar_arista('Comedor', 'Sala de estar', 7)
grafo.insertar_arista('Comedor', 'Terraza', 24)
grafo.insertar_arista('Cochera', 'Patio', 5)
grafo.insertar_arista('Cochera', 'Quincho', 9)
grafo.insertar_arista('Cochera', 'Terraza', 6)
grafo.insertar_arista('Quincho', 'Patio', 3)
grafo.insertar_arista('Quincho', 'Baño 2', 7)
grafo.insertar_arista('Quincho', 'Sala de estar', 35)
grafo.insertar_arista('Baño 1', 'Patio', 10)
grafo.insertar_arista('Baño 1', 'Terraza', 6)
grafo.insertar_arista('Baño 1', 'Habitacion 2', 7)
grafo.insertar_arista('Habitacion 2', 'Quincho', 15)
grafo.insertar_arista('Habitacion 2', 'Baño 2', 20)
grafo.insertar_arista('Habitacion 2', 'Patio', 10)
grafo.insertar_arista('Patio', 'Terraza', 10)
grafo.insertar_arista('Patio', 'Habitacion 1', 4)
grafo.insertar_arista('Patio', 'Baño 2', 12)
grafo.insertar_arista('Habiacion 1', 'Salsa de estar', 4)
grafo.insertar_arista('Habitacion 1', 'baño 1', 9)

#print(grafo.barrido_amplitud('Cocina'))


ArbolMin = grafo.kruskal()
#print(ArbolMin)
ArbolMin = ArbolMin[0].split("-")
peso_total = 0
for nodo in ArbolMin:
     nodo = nodo.split(";")
     #print(nodo)
     peso_total += int(nodo[2])
     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print('Para conectar todo el ambiente se necesita: ',peso_total)


camino = grafo.dijkstra('Habitacion 1') #dijkstra nos da el camino mas corto 
CaminoCorto = grafo.camino(camino, 'Habitacion 1', 'Sala de estar')
print(CaminoCorto)
