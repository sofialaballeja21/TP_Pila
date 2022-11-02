'''15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica);
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido.'''

from grafo import Grafo

grafo = Grafo(dirigido=False)

#A
#Maravillas naturales

grafo.insertar_vertice('Cataratas del Iguazu', datos={'tipo': 'n', 'pais': 'Argentina-Brasil'})
grafo.insertar_vertice('Amazonia', datos={'tipo': 'n', 'pais': 'Bolivia-Brasil-Colombia-Ecuador-Guyana-Perú-Surinam-Venezuela'})
grafo.insertar_vertice('Bahía de HanLong', datos={'tipo':'n', 'pais': 'China'})
grafo.insertar_vertice('Isla Jeju', datos={'tipo': 'n', 'pais': 'Corea del Sur'})
grafo.insertar_vertice('Parque Nacional de Komodo', datos={'tipo': 'n', 'pais': 'Indonesia'})
grafo.insertar_vertice('Montaña de la Mesa', datos={'tipo': 'n', 'pais':' Sudáfrica'})
grafo.insertar_vertice('Parque Nacional del río subterráneo de Puerto Princesa', datos={'tipo': 'n', 'pais': 'Filipinas'})

#Maravillas Arquitectonicas
grafo.insertar_vertice('Estatua de Cristo Redentor', datos={'tipo': 'a', 'pais': 'Brasil '})
grafo.insertar_vertice('Machu Picchu', datos={'tipo': 'a', 'pais': 'Perú '})
grafo.insertar_vertice('La Gran Muralla China', datos={'tipo': 'a', 'pais': 'China'})
grafo.insertar_vertice('Ciudad de Petra', datos={'tipo': 'a','pais': 'Jordania'})
grafo.insertar_vertice('Taj Mahal', datos={'tipo': 'a', 'pais': 'India '})
grafo.insertar_vertice('El Coliseo romano', datos={'tipo': 'arq', 'pais': 'Italia'})
grafo.insertar_vertice('Chichén Itzá', datos={'tipo': 'a', 'pais': 'México'})
grafo.insertar_vertice('hfur', datos={'tipo': 'a', 'pais': 'India'})

#B
#Distancia de las maravillas naturales
grafo.insertar_arista('Cataratas del Iguazu', 'Amazonia', 3000)
grafo.insertar_arista('Amazonia', 'Bahía de Han-Long', 7857)
grafo.insertar_arista('Bahía de HanLong', 'Isla Jeju', 9452)
grafo.insertar_arista('Isla Jeju', 'Parque Nacional de Komodo', 5640)
grafo.insertar_arista('Parque Nacional de Komodo', 'Montaña de la Mesa', 29.888 )
grafo.insertar_arista('Montaña de la Mesa', 'Parque Nacional del río subterráneo de Puerto Princesa',7222)
grafo.insertar_arista('Parque Nacional del río subterráneo de Puerto Princesa', 'Cataratas del Iguazu', 34980)

#Distanciade las maravillas arquitectonicas
grafo.insertar_arista('Estatua de Cristo Redentor', 'Machi PiCchu', 3463)
grafo.insertar_arista('Machu Picchu', 'La Gran Muralla China', 39232)
grafo.insertar_arista('La Gran Muralla China', 'Ciudad de Petra', 98453)
grafo.insertar_arista('Ciudad de Petra', 'Taj Mahal', 9234)
grafo.insertar_arista('Taj Mahal', 'El Coliceo romano', 87342)
grafo.insertar_arista('El Coliceo romano', 'Chichén Itzá', 10983)
grafo.insertar_arista('Chichén Itzá', 'Estatua de Cristo Redentor', 23745)
grafo.insertar_arista('hfur', 'Machu Picchu', 2342)

#C
Arbol = grafo.kruskal()
#print(Arbol)

#Kruskal natural
'''ArbolNat = Arbol[0].split("-")
peso_total = 0
for nodo in ArbolNat:
     nodo = nodo.split(";")
     print(nodo)
     peso_total += int(nodo[2])
     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print('Kruskal de maravillas naturales:', peso_total)


#Kruskal Arquitectonico
ArbolArq = Arbol[0].split("-")
peso = 0
for nodo in ArbolArq:
     nodo = nodo.split(";")
     print(nodo)
     peso += int(nodo[2])
     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print('Kruskal de maravillas arquitectonico:', peso)'''

#D
paises = grafo.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])
    
#E
maravillas = grafo.maravilla_mismo_tipo()
for mara in maravillas:
     print(mara, maravillas[mara])