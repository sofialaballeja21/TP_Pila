from lista import Lista
from jurassic_parkkk import dinosaurs
from cola import Cola

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name'], dino['type']


class Dinosaurio:
    def __init__(self, fecha, codigo, nombre, level, type):
        self.nombre = nombre
        self.fecha = fecha
        self.codigo = codigo
        self.level = level
        self.type = type

    def __str__(self):
        return f"nombre: {self.nombre}, fecha: {self.fecha}, zona: {self.codigo}, level: {self.level}, type: {self.type}"

lista_fecha = Lista()
lista_nombre = Lista()
cola1 = Cola()
cola2 = Cola()

file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    name, type = busqueda(dato[2])
    dino = Dinosaurio(dato[0], dato[1], name, dato[3], type)
    lista_fecha.insertar(dino, 'fecha')
    lista_nombre.insertar(dino, 'nombre')
    if(dino.level in ['critical', 'high']):
        if(dino.type == 'carnívoro '):
            cola1.arribo(dino)
        else:
            cola2.arribo(dino)

#lista_fecha.barrido()
#print()
#lista_nombre.barrido()

park = ['Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus']
lista_nombre.barrido_level(park, ['high', 'critical'])
print()

zonas = ['WYG075', 'SXH966', 'LYF010']
for zona in zonas:
    dato = lista_fecha.eliminar(zona, 'codigo')
    if dato:
        print(f'{dato} eliminada de la lista fecha')
    dato = lista_nombre.eliminar(zona, 'codigo')
    if dato:
        print(f'{dato} eliminada de la lista nombre')


pos = lista_fecha.busqueda('HYD195', 'codigo')
if pos:
    pos.info.nombre = 'nombre'

pos = lista_nombre.busqueda('HYD195', 'codigo')
if pos:
    dato = lista_nombre.eliminar('HYD195', 'codigo')
    dato.nombre = 'nombre'
    lista_nombre.insertar(dato, 'nombre')
    
print('----------------------------------------------')

lista_fecha.barrido()
print('------------------------------------------------')
lista_nombre.barrido()
print('-------------------------------------------------')

dinos = ['Compsognathus','Carnotaurus','Raptors (Dromaeosauridae)',]
lista_nombre.barrido_nivel(dinos, ['high', 'critical', 'low', 'medium'])

print()
clave = 'mosquito'

def decodificar(num):
    if(num >= 33 and num <= 47):
        return chr(numero)
    else:
        if(numero % 3 == 0):
            return decodificar(num // 2 + 9)
        else:
            return decodificar(num-14)

clave_deco = ''
for palabra in clave:
    numero = ord(palabra)
    clave_deco += decodificar(numero)

print(f'clave decodificada: {clave_deco}')

print('---')
while(not cola1.cola_vacia()):
    dato = cola2.atencion()
    if(dato.codigo == 'EPC944'):
        print(' ha el dato ha sido borrado')
    else:
        print(dato)
print('---')
while(not cola1.cola_vacia()):
    dato = cola2.atencion()
    if(dato.codigo == 'EPC944'):
        print(' ha el dato ha sido borrado')
    else:
        print(dato)
        
'''def barrido_nivel(self, dino, nivel):  #pertenece al parcial
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre in dino and aux.info.level in nivel):
                print(aux.info)
            aux = aux.sig'''
