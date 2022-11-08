'''Se dispone de una lista de todos los Jedi, 
de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar 
las funciones necesarias para resolver las
actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;---------
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;------------
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir 
sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
'''
from lista import Lista
class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()


lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    # datos.pop(-1)
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')

                  
# A
#lista_jedi.barrido()
print()
# lista_jedi2.barrido()

#B
'''dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

dato = lista_jedi.busqueda('ahsoka tano', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')
print()
'''

#C
print('----- Barrido aprendices de yoda y luke -----')
lista_jedi.barrido_jedi_master()
print()

#D mostrar los Jedi de especie humana y twi'lek;
print('----- Barrido especies human y twi lek -----')
lista_jedi2.barrido_especie()
print()

#E
print('----- Barrido empieza con A -----')
lista_jedi.barrido_comienza_con(['a'])
print()

#F. mostrar los Jedi que usaron sable de luz de más de un color;


#G. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print('----- Barrido color del sable yellow o violet -----')
lista_jedi2.barrido_sable()
print()


#H. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print('------ Barrido padawans de Qui-Gon Jin y Mace Windu')
lista_jedi.maestros()


