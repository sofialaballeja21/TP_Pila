from lista import Lista

#EJERCICIO_21

class peliculas:
    def __init__(self, Nombre, Valoracion, AñoEstreno, Recaudacion):
        self.Nombre = Nombre
        self.Valoracion = Valoracion
        self.AñoEstreno = AñoEstreno
        self.Recaudacion = Recaudacion
        
    def __str__(self):
        return f"{self.Nombre} - {self.Valoracion} - {self.AñoEstreno} - {self.Recaudacion}"
    

lista_peliculas = [{'Nombre': 'Star Wars', 'Valoracion': 9, 'Año de estreno': 1977, 'Recaudacion': 10000000},
                   {'Nombre': 'Pantera Negra', 'Valoracion': 8, 'Año de estreno': 2018, 'Recaudacion': 1347000000},
                   {'Nombre': 'Buscando a Dory', 'Valoracion': 10, 'Año de estreno': 2016, 'Recaudacion': 1028570889},
                   {'Nombre': 'Inseparables', 'Valoracion': 7, 'Año de estreno': 2016, 'Recaudacion': 15675000},
                   {'Nombre': 'Doctor Strange', 'Valoracion': 9, 'Año de estreno': 2016, 'Recaudacion': 17226000000},
                   {'Nombre': 'Jurassic World', 'Valoracion': 8, 'Año de estreno': 2018, 'Recaudacion': 7444000000},
                   {'Nombre': 'Mulan 2', 'Valoracion': 10, 'Año de estreno': 2004, 'Recaudacion': 4926000000},
                   {'Nombre': 'Talentos Ocultos', 'Valoracion': 10, 'Año de estreno': 2016, 'Recaudacion': 12986000000},
                   {'Nombre': 'Espanta Tiburones', 'Valoracion': 10, 'Año de estreno': 2004, 'Recaudacion': 4527000000},
                   {'Nombre': 'Aquaman', 'Valoracion': 6, 'Año de estreno': 2018, 'Recaudacion': 1226000000}]


listas = Lista()
lista_aux = Lista()

for lis in lista_peliculas:
    listas.insertar(peliculas(lis['Año de estreno'],
                              lis['Nombre'],
                              lis['Valoracion'],
                              lis['Recaudacion']), 'Nombre')
 

print(listas.tamanio())

#a
estreno = int(input('Ingrese el año por el que desea filtrar las peliculas: '))
print(listas.barrido_anio(estreno))


#b
print()
print("Pelicula con mayor recaudacion:",listas.mayor('Recaudacion').info)
#c
print()
print("Películas con mayor valoración del público: ", listas.copiar(lista_aux, 'Valoracion'))

#d
print("Lista ordenada por Nombre: ")
listas.barrido()
print()
print("Lista ordenada por recaudacion: ")
listas.copiar(lista_aux,'Recaudacion')
lista_aux.barrido()
lista_aux.vaciar()
print()
print("Lista ordenada por año de estreno: ")
listas.copiar(lista_aux,'AñoEstreno')
lista_aux.barrido()
lista_aux.vaciar()
print()
print("Lista ordenada por valoracion del publico: ")
listas.copiar(lista_aux,'Valoracion')
lista_aux.barrido()




