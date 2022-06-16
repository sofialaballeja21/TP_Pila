
from jurassic_park import dinosaurs
from Listas import Lista
from pila import Pila
from cola import Cola

class dino():
    hora, zona, numero, estado, nombre = None, None, None,None, None
    
    def __str__(self):
        return f'{park.hora}, {park.zona}, {park.numero}, {park.estado}, {park.nombre}'

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']

pila = Pila()
lista_jurassic = Lista()
lista = Lista()
cola_carnivoros = Cola()
cola_hervivoros = Cola()

file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)
 
for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    
    park = dino()
    park.hora   = dato[0]
    park.zona   = dato[1]
    park.numero = dato[2]
    park.estado = dato[3]
    park.nombre = dato[4]
    
    a = (f'{park.hora}, {park.zona}, {park.numero}, {park.estado}, {park.nombre}')
    print(park.hora, park.zona, park.numero, park.estado, park.nombre)
    pila.apilar(park)
    print(park)
#print(pila.tamanio())

    
while (not pila.pila_vacia()):
   park = pila.desapilar()
 #Simon Masrani  
   if (park.nombre == 'Tyrannosaurus Rex' and park.estado == 'critical' ):
       print(f'Tirannosaurus Rex con estado critical:  {park.hora}, {park.zona}, {park.numero} ')
       
   if (park.nombre == 'Giganotosaurus' and park.estado == 'critical'):   
         print(f'Giganotosaurus con estado critical:  {park.hora}, {park.zona}, {park.numero}')
    
   if (park.nombre == 'Spinosaurus' and park.estado == 'critical'):
           print(f'Spinosaurus con estado critical:  {park.hora}, {park.zona}, {park.numero}') 
             
   if (park.nombre == 'Tyrannosaurus Rex' and park.estado == 'high'):
       print(f'Tyrannossaurus Rex con estado high: {park.hora}, {park.zona}, {park.numero}')   
  
   if (park.nombre == 'Spinosaurus' and park.estado == 'high'):   
         print(f'Sapitnosaurus con estado high:  {park.hora}, {park.zona}, {park.numero}')
 
   if (park.nombre == 'Giganotosaurus' and park.estado == 'high'):   
         print(f'Giganotosaurus con estado high:  {park.hora}, {park.zona}, {park.numero}')    
