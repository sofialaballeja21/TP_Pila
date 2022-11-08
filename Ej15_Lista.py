'''Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;'''

from lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return self.nombre

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]

# Tyrantrum, Te-rrakion o Wingull
for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
print()   


#A
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
     print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
else:
    print('el entrenador no esta en la lista')


#!B
lista_entrenadores.barrido_entrenador_mas_tres()
print()

# C
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
print()

#D
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.info}")
    print('sus pokemons')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()

#E
lista_entrenadores.barrido_porcentaje_victorias()

#F. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print('Entrenadores con pokemones de tipo fuego y planta o agua/volador')
lista_entrenadores.barrido_TipoySubtipo()

#G. el promedio de nivel de los Pokémons de un determinado entrenador;
poke = input('Ingrese el nombre del entrenador para calcular el promedio: ')
lista_entrenadores.busqueda(poke, 'nombre')
if (poke):
    print('Promedio de el entrenaodr: ', lista_entrenadores.promedio())
    
#H. determinar cuántos entrenadores tiene un determinado Pokémon;
pokem = input('Ingresar pokemon: ')
print(lista_entrenadores.barrido_entrenadores(pokem), 'entrenadores', pokem)

#I. mostrar los entrenadores que tienen Pokémons repetidos;



#J. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-rrakion o Wingull;

lista_entrenadores.pokemons('Tyrantrum', 'Te-rrakion' 'Wingull')

#Kk. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#deberán mostrar los datos de ambos
entrenador_Y = input('Ingrese el nombre del pokemon')
entrena = lista_entrenadores.busqueda(entrenador_Y, 'nombre')
if (entrena):
    pokemones = input('Ingrese elnombre del pokemon: ')
    if (pokem):
        print('Datos entrenadoR: ', entrenador_Y.info.nombre, entrenador.info)
        print('Datos del pokemon: ',  pokemones.info.nombre, pokemones.info)
    else:
        print('El entrenador no tiene ese pokemon')
else:
    print('No existe ese entrenador')




