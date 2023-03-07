from ListaSimple import *
from colour import Color
from randomcolor import RandomColor

arreglos = ListaSimple()

arreglos.AgregarCabeza(222)
arreglos.AgregarCabeza(23)
arreglos.AgregarCabeza(24)
arreglos.AgregarCabeza(224)
arreglos.EliminarCabeza()
arreglos.AgregarCabeza(224)# revisar función
arreglos.recorrido()
print("++++++++")

for i in range(arreglos.tamaño()):
    print(arreglos.invocar(i))

print("****************************")

# pruebas
print("cabeza de la lisata ",arreglos.cabeza.getDato())
print("cola de la lista",arreglos.cola.getDato())









# Crear un rango de 1000 colores entre blanco y negro
colores = list(Color('white').range_to(Color('black'), 1000))

# Obtener el nombre del color en el índice 500
color_nombre = str(colores[500])

print(color_nombre) # imprime "rgb(0.501961, 0.501961, 0.501961)"


"""
obj = arreglos.cola

obj = obj.getDirection()

obj2 = obj

obj2= obj2.getDirection()
print("dato despues de la cola es ",obj.getDato())
print("despues ",obj2.getDato())
"""

print("++++++++++++++++++++++++")
for i in range(5,6):
  print(i)

print("--------------------------------------------")
colores = []
rc = RandomColor()
      
colors = rc.generate(count=3)
      
for i in range(len(colors)):
  colores.append(colors[i])
for j in range(len(colores)):
   print(colores[j])  