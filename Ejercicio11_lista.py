'''11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la si-
guiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que
apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:'''

from lista import Lista

class personajes:
    def __init__(self, nombre, altura, edad, genero, especie,planeta, episodio):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodio = episodio
        
    def __str__(self):
        return f"{self.nombre} - {self.altura}- {self.edad} - {self.genero} - {self.especie} - {self.planeta} - {self.episodio}"

descripcion = [{'nombre': 'julia', 'altura': 23, 'edad': 432, 'genero': 'femenino', 'especie': 'droide', 'planeta': 'jupiter', 'episodio': 7},
        {'nombre': 'Darth Vader', 'altura': 170, 'edad': 900, 'genero': 'masculino', 'especie': 'jedi', 'planeta': 'neptuno', 'episodio': 67},
        {'nombre': 'samanta', 'altura': 65, 'edad': 895, 'genero': 'femenino', 'especie': 'droide', 'planeta': 'alderaan', 'episodio': 1},
        {'nombre': 'Han Solo', 'altura': 43, 'edad': 500, 'genero': 'masculino', 'especie': 'jedi', 'planeta': 'urano', 'episodio': 15},
        {'nombre': 'julia', 'altura': 181, 'edad': 859, 'genero': 'femenino', 'especie': 'humano', 'planeta': 'alderaan', 'episodio': 98},
        {'nombre': 'Chewbacca', 'altura': 180, 'edad': 300, 'genero': 'masculino', 'especie': ' wookiee', 'planeta': 'Kashyyyk', 'episodio': 6}
        ]   

lista_personajes = Lista()

for linea in descripcion:
    lista_personajes.insertar(personajes(linea['nombre'],
                                         linea['altura'],
                                         linea['edad'],
                                         linea['genero'],
                                         linea['especie'],
                                         linea['planeta'],
                                         linea['episodio']), campo = 'nombre')
    
lista_personajes.barrido()


#a. listar todos los personajes de género femenino;
print()
print('Listado femenino')
lista_personajes.barrido_femenino()

#b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episo-dios de la saga;
print()
print('Listado de droides')
lista_personajes.barrido_droide()

#c. mostrar toda la información de Darth Vader y Han Solo;
print()
dato = lista_personajes.busqueda('Darth Vader', 'nombre')
if dato:
    print(f"Datos de: {dato.info}")
else:
    print("Darth Vader no esta en la lista")
print()
dato = lista_personajes.busqueda('Han Solo', 'nombre')
if dato:
    print(f"Datos de: {dato.info}")
else:
    print('Han Solo no esta en la lista')
print()

#d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
print('Listado de los personajes de los capitulos 7, 6, 5')
lista_personajes.barrido_episodio()
print()

#e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
print('Personajes mayor a 850 años y el mayor de ellos')
lista_personajes.barrido_mayor_850()
print()

#f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
print('Episodios eliminados:')
epi = ['4', '5', '6']

for elimi in epi:
    datos = lista_personajes.eliminar(elimi, 'episodio')
    if datos:
        print(f"--episodio {datos} eliminado de la lista")
print()


#g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;             
print('Personajes humanos del planeta Alderaan')
lista_personajes.barrido_humanos()
print()      
        
#h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
print('Personajes menores de 70cm')
lista_personajes.barrido_altura()       
print()

#i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
print('Busqueda de: ')
lista_personajes.buscar_Chewbacca()


