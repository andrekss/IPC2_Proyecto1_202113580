from graphviz import *
from PaintOrganismos import *

class Tablero:

    def __init__(self,xVisualizar,yVisualizar):
        self.xVisualizar = xVisualizar
        self.yVisualizar = yVisualizar
        self.dot = Digraph(comment='tablero', format='pdf') #plantilla para el tablero

    def CargaTablero(self):
        for i in range(self.yVisualizar):
          for j in range(self.xVisualizar): 
           h = i+1
           self.dot.node(f'{i},{j}', shape='square', width = '0.1', height= '0.1')
           if h <= self.yVisualizar-1:
            self.dot.node(f'{h},{j}', shape='square', width = '0.1', height= '0.1')
            self.dot.edge(f'{i},{j}',f'{h},{j}',arrowhead = 'none',arrowsize = '0.01')   
       # self.dot.node('0,0', shape='square', width = '0.1', height= '0.1',fillcolor='green', style="filled")          
        #self.dot.render('Tablero', view=True)  

    def actualizar(self, Load, listo,renderizar):
       if listo == True: 
        self.xVisualizar = int(input("Introduzca el número de columnas que quiere visualizar: "))
        self.yVisualizar = int(input("Introduzca el número de filas que quiere visualizar: ")) 
       self.CargaTablero()
       self.Orgas = Organismos(self.dot,Load.ListaMuestras,Load.ListaOrganismos)
       
       self.Orgas.GenerarOrganismos(renderizar) 