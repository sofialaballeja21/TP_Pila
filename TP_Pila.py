from pila import Pila

pila = Pila()
#19
class peliculas():
    titulo, estreno, estudio = None, None, None


titulo = ['iron man I,', 'Batman,','linterna verde,', 'Dr. Strange,', 'Spider-Man: Homecoming,', 'Capitan America: Civil War,','Mujer maravilla,']
estreno = [2016, 2018, 2014, 2014, 2018, 2016, 2016]
estudio = [' Marvel', 'DC', 'DC', 'Marvel',' Marvel', 'Marvel','DC']


pelicula = [
    {'titulo': 'iron man', 'estreno': 2016, 'estudio': 'Marvel', },
    {'titulo': 'batman', 'estreno': 2016, 'estudio': 'Dc', },
    {'titulo': 'linterna verde', 'estreno': 2016, 'estudio': 'DC',},
    {'titulo': 'capitan america', 'estreno': 2014, 'estudio': 'Marvel', },
    {'titulo': 'wolverine', 'estreno': 2018, 'estudio': 'Marvel', },
    {'titulo': 'dr. strange', 'estreno': 2018, 'estudio': 'DC', },
    {'titulo': 'mujer maravilla', 'estreno': 2014, 'estudio': 'DC',}]

from random import choice

for i in range(len(pelicula)):
    dato = peliculas()
    dato.titulo = titulo[i]
    dato.estreno = estreno[i]
    dato.estudio = estudio[i]
    dic = {'titulo': titulo[i], 'estreno': estreno[i], 'estudio': estudio[i]}
    print(dato.titulo, dato.estreno, dato.estudio)
    pila.apilar(dato)
        
    
cont = 0
while(not pila.pila_vacia()):
    dato = pila.desapilar()
    # A 
    if(dato.estreno == 2014):
        print(f'La pelicula {dato.titulo} fue estrenada en 2014')
    #else: 
    #    print('No se estrenaron peliculas en 2014')
    
    # B
    if(dato.estreno == 2018):
        cont += 1
        
    #C  
    if(dato.estudio == 'Marvel' and dato.estreno == 2016):
        print(f'{dato.titulo} fue estrenada en Marvel Studio en 2016')
    #else: 
    #    print('No hay peliculas de Marvel Studio estrenadas en 2016')

print('Las veces que se estrenaron peliculas en 2018 fueron: ', cont)





#24
class MARVEL():
    personaje, participacion= None, None


personaje = ['Groot', 'Rocket Raccoon','Tony Stark', 'Peter Parker','Viuda Negra', 'Steven Strange','Loki', 'Nick Furia','Gamora' ]
participacion = [5,5, 7, 5, 3, 3, 8, 5, 6]


MCU = [
    {'personaje': 'Tony Stark', 'participacion': 4 },
    {'personaje': 'Peter Parker', 'participacion': 7},
    {'personaje': 'Groot', 'participacion': 5},
    {'personaje' : 'Rocket Raccoon', 'participacion':5},
    {'personaje': 'Viuda Negra', 'participacion': 3},
    {'personaje': 'Steve Strange', 'participacion':3},
    {'personaje': 'Loki', 'participacion': 8},
    {'personaje': 'Nick Furia', 'participacion': 5},
    {'personaje': 'Gamora', 'participacion': 6}]

from random import choice

for i in range(len(MCU)):
    dato = MARVEL()
    dato2 = MARVEL()
    dato.personaje = personaje[i]
    dato.participacion = participacion[i]

    dic = {'personaje': personaje[i], 'participacion': participacion[i]}
    print(dato.personaje, dato.participacion)
    pila.apilar(dato)
Cont_Groot = pila.tamanio() + 1
Cont_Rocken = pila.tamanio() + 1
#print(pila.tamanio())

while(not pila.pila_vacia()):
    dato = pila.desapilar()
   # print(dato.personaje)
    Cont_Groot -=1
    Cont_Rocken -= 1
    
    #A
    if (dato.personaje == 'Groot'):
       print('Groot se encuentra en la posicion: ', Cont_Groot)
       
    Cont_Rocken -= 1 
    if(dato.personaje == 'Rocket Raccoon'):
        print('Rocket Raccoon se encuentra en la posicion: ', Cont_Rocken )
        
    #B
    if (dato.participacion > 5):
        print(f'Los personajes que participaron más de 5 veces son: {dato.personaje} y participo {dato.participacion} peliculas ')    
    # C
    if (dato.personaje == 'viuda negra'):
        print(f'La Viuda negra participo en {dato.participacion} peliculas')
    
    # D
    if (dato.personaje[0] == 'C'):
        print(f'{dato.personaje}, inicia con la letra: C')
        
    elif(dato.personaje[0] == 'D'):
        print(f'{dato.personaje}, inicia con la letra: C')
    
    elif (dato.personaje[0] == 'G'):
        print(f'{dato.personaje}, inicia con la letra: G')
    
        