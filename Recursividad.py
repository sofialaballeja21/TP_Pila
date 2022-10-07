#NÚMEROS ROMANOS

'''valor ={'I': 1, 'V':5,'X': 10, 'L': 50, 'C': 100}
def num_romano(romano):
   if (len(romano)== 1):
       return valor[romano[0]]
   elif (valor[romano[0]] >= valor[romano[1]]):
       return valor[romano[0]] + num_romano(romano[1:])
   else:
        return -valor[romano[0]] + num_romano(romano[1:])
print(num_romano('XL'))'''



#USAR LA FUERZA
mochila = ( 'blaster', 'lanza misiles', 'blaster de iones', 'sable de luz', 'ballesta de Chewbacca', 'gaderffii')

def usar_la_fuerza(vector, buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector)-1
    else: return usar_la_fuerza(vector[:-1], buscado)
print(usar_la_fuerza( mochila, 'sable de luz'))



#LABERINTO
'''def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1
lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [0, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]
salida_laberinto(lab, 0, 0)'''
