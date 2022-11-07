'''Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a.cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión.'''



from heap import HeapMin
from heap import HeapMax

heap = HeapMax()
h = HeapMax()

#A
heap.agregar('DocumentoEmpleado1', 1)
heap.agregar('DocumentoEmpleado2', 1)
heap.agregar('DocumentoEmpleado3', 1)

#B
print('Primer elemeno de la cola', heap.vector[0])

#C
heap.agregar('DocumentoStaff1', 2)
heap.agregar('DocumentoStaff2', 2)

#D
heap.agregar('DocumentoGerente1', 3)

#e
print('Primer y segundo elemento de la cola: ', heap.vector[0],'y', heap.vector[1])

#F
heap.agregar('DocumentoEmpleado4', 1)
heap.agregar('DocumentoEmpleado5', 1)
heap.agregar('DocumentoGerente2', 3)

#G
print('Toda la cola de impresion: ')
print(heap.vector)




