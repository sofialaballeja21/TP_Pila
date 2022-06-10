from cola import Cola

cola1 = Cola()

class MCU():
    personaje, nombre_super, genero = None, None, None

personajes =    ['Black Window', 'Capitan America', 'Capitana Marvel', 'Deadpool', 'Hulk', 'Wanda', 'Loki', 'Ant-Man']
nombre = ['Natasha Romanoff', 'Steve Rogers', 'Carol Danvers', 'Wade Wilson', 'Bruce Banner', 'Wanda Maximoff', 'Loki Laufeyson','Scott Lang']
gen =       ['F', 'M', 'F', 'M', 'M', 'F', 'M', 'M']


for i in range(len(personajes)):
    dato = MCU()
    dato.personaje = personajes[i]
    dato.nombre_super = nombre[i]
    dato.genero = gen[i]
    print(dato.personaje, dato.nombre_super, dato.genero)
    cola1.arribo(dato)
#print(cola1.tamanio())

while(not cola1.cola_vacia()):    
    dato = cola1.atencion()
    #!A
    if (dato.personaje == 'Capitana Marvel' ):
       print(f'El nombre del personaje de Capitana Marvel es, ', dato.nombre_super)
    #!B
    if (dato.genero[0] == 'F'):
       print(f'{dato.personaje} es un personaje femenino')
    #else: 
    #    print('No hay personajes femeninos')
    #!C
    if (dato.genero[0] == 'M'):
       print(f'{dato.personaje} es un personaje masculino')
    #else: 
    #    print('No hay personajes masculinos')
    #!D
    if (dato.nombre_super == 'Scott Lang'):
       print(f'El nombre de superheroe de Scott Lang es: {dato.personaje}')
    #else: 
    #    print('Scott Lang no fue cargado')
    #!E    
    if (dato.nombre_super[0] == 'S' or dato.personaje[0] == 'S'):
       print(f'{dato.personaje} se llama {dato.nombre_super} y sugenero es {dato.genero}')
    #else: 
    #    print('No hay personajes o nobres con S')
    #!F
    if (dato.nombre_super == 'Carol Danvers'):
        print(f'Carol Danvers es {dato.personaje}')
