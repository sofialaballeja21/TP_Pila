'''Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos'''


from cola import Cola
import random  
import string

variable = string.ascii_uppercase
variable_A = string.digits


cola = Cola()     
cola_1 = Cola()
cola_2 = Cola()


def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_uppercase) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    
    #random.shuffle(sample_list) #mezcla la lista entre numros y letras
    
    # convert list to string
    final_string = ''.join(sample_list)
    print('Turno: ', final_string)


for i in variable:
  dato = get_string
  dato.letters = variable()
  dato.digits = variable_A
  get_string(1,3)
  cola.arribo(dato)
  
print(cola.tamanio())

while not cola.cola_vacia():
  dato = cola.atencion()
  
  if dato.letters == 'A' or dato.letters == 'a':
    cola_1.arribo(dato)
    print('Datos de la cola 1')
    print('Turno: ', dato.letters + dato.digits)
    
  elif dato.letters == 'C' or dato.letters == 'c':
    cola_1.arribo(dato)
    print('Datos de la cola 1')
    print('Turno: ', dato.letters + dato.digits)
    
  elif   dato.letters == 'F' or  dato.letters == 'f':
    cola_1.arribo(dato)
    print('Datos de la cola 1')
    print('Turno: ', dato.letters + dato.digits)
    
  elif dato.letters == 'B' or dato.letters == 'b':
    cola_2.arribo(dato)
    print('Datos cola 2')
    print('Turno: ')
    
  elif dato.letters == 'D' or dato.letters == 'd': 
    cola_2.arribo(dato)
    print('Datos cola 2')
    print('Turno: ')
    
  elif dato.letters == 'E' or  dato.letters == 'e':
    cola_2.arribo(dato)
    print('Datos cola 2')
    print('Turno: ')
    
  print(cola.tamanio())
