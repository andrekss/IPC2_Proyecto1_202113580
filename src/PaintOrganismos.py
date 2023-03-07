from graphviz import *
from ListaSimple import *
from MainListas import *
from randomcolor import *

class Organismos:

    def __init__(self, dot, listaMuestras,listaOrganismos):
        self.dot = dot
        self.listaMuestras= listaMuestras
        self.listaOrganismos = listaOrganismos
        
        

    def colores(self,i,j):
      self.Colores = ListaSimple()

      self.Colores.AgregarCabeza('red')
      self.Colores.AgregarCabeza('yellow')
      self.Colores.AgregarCabeza('blue')
      self.Colores.AgregarCabeza('green')
      self.Colores.AgregarCabeza('black')
      self.Colores.AgregarCabeza('orange')
      self.Colores.AgregarCabeza('pink')
      self.Colores.AgregarCabeza('brown')
      self.Colores.AgregarCabeza('cyan')
      self.Colores.AgregarCabeza('lavender')
      self.Colores.AgregarCabeza('turquoise')
      self.Colores.AgregarCabeza('magenta')
      self.Colores.AgregarCabeza('teal')
      self.Colores.AgregarCabeza('maroon')
      self.Colores.AgregarCabeza('gold')
      self.Colores.AgregarCabeza('navy')
      self.Colores.AgregarCabeza('silver')
      self.Colores.AgregarCabeza('crimson')
      self.Colores.AgregarCabeza('violet')
      self.Colores.AgregarCabeza('indigo')
      self.Colores.AgregarCabeza('orchid')
      self.Colores.AgregarCabeza('skyblue')
                       
      
      for h in range(self.Colores.tamaño()):  
         if int(self.listaMuestras.invocar(i).ListaCeldasVivas.invocar(j).codigoOrganismo) == (h+1):
             return self.Colores.invocar(h)
    
    def GenerarOrganismos(self,renderizar):
        self.dot.node('Muestras seleccionadas',fillcolor="purple", style="filled",fontcolor="yellow",fontsize="20")

        for i in range(self.listaMuestras.tamaño()): 
         for j in range(self.listaMuestras.invocar(i).ListaCeldasVivas.tamaño()):
           color = self.colores(i, j)      
           self.dot.node(f'{self.listaMuestras.invocar(i).ListaCeldasVivas.invocar(j).fila},{self.listaMuestras.invocar(i).ListaCeldasVivas.invocar(j).columna}', shape='square', width = '0.1', height= '0.1',fillcolor=f'{color}', style="filled")            

        for h in range(self.listaOrganismos.tamaño()):
         metodo = self.Colores.invocar(h)
         self.dot.node(f'{self.listaOrganismos.invocar(h).nombre}, código {self.listaOrganismos.invocar(h).codigo}',fillcolor=f"{metodo}", style="filled",fontcolor="white",fontsize="20",penwidth='2', pencolor='black')
       
        for x in range(self.listaOrganismos.tamaño()):
          y= x+1
          if y < self.listaOrganismos.tamaño():
           self.dot.edge(f'{self.listaOrganismos.invocar(x).nombre}, código {self.listaOrganismos.invocar(x).codigo}', f'{self.listaOrganismos.invocar(y).nombre}, código {self.listaOrganismos.invocar(y).codigo}', dir="back") 
       
        if renderizar == True: 
         self.dot.render('Tablero', view=True)




    def GenerarPrueba(self,x,y,codigo, existeee):
       self.dot.node(f'{x},{y}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")
       if existeee == True: 
        self.dot.render('Tablero', view=True)

    def verificacionExiste(self,columna,fila):
     self.a= True
     for j in range(self.listaMuestras.tamaño()): 
      for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
          if columna == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fila :   
                 self.a=False
                 return False
     if self.a == True:  
              return True 

    def Prosperar(self,fila,columna,codigo,ncodigo,ModoProsperar): #colocar despues -> filaOriginal
       self.prosperará=False
       validaciones = 8

       for i in range(validaciones):
        if i == 0: #verificar derecha, columna sumar a la derecha
          #print("ESTAS AQUI "+str(ncodigo))
         entraste=False
         col = columna
         col += 1 
         avisar = True
         if self.verificacionExiste(columna,fila):  
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              
              if col == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fila :
        
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 col += 1
                 if (columna+1)==col:
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and col>(columna+1):
                 
                if ModoProsperar == True:
                 entraste = True
                 for l in range(columna+1,col): #en la
                  if avisar:
                   for h in range(100):
                    for a in range(self.listaMuestras.tamaño()): 
                     for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                      if fila == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                       self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1
                  self.dot.node(f'{fila},{l}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                
                 if avisar:
                  contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                  print("--------La muestra prosperará--------")
                  self.prosperará=True
                  self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar=False
                 break
                else:
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")                 
                 break          
          if entraste == True:
           self.dot.render('Tablero',view=True)    
        
        elif i ==1: #verificar izquierda, columna restar a la izquierda
         entraste1=False
         col1 = columna
         col1 -= 1 
         avisar1 = True
         if self.verificacionExiste(fila,columna) :
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              
              if col1 == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fila :
  
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 
                 col1 -= 1 
                 if (columna-1)==col1:
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and col1<(columna-1) :
                
                if ModoProsperar == True:
                 entraste1 = True
                 for l in range(col1,columna): #en la
                  if avisar1 == True:
                   for h in range(100):
                    for a in range(self.listaMuestras.tamaño()): 
                     for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                      if fila == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                       self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1
                  self.dot.node(f'{fila},{l}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                
                 if avisar1 == True:
                   contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                   print("--------La muestra prosperará--------")
                   self.prosperará=True
                   self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar1 = False 
                 break 
                else:
              
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled") 
                 break          
          if entraste1 == True:
           self.dot.render('Tablero',view=True)
        elif i ==2: #verificar abajo, fila sumara hacia abajo
         entraste2=False
         fil = fila
         fil += 1 
         avisar2 = True
         if self.verificacionExiste(fila,columna) :
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):         
              if columna == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil :
  
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 fil += 1 
                 if fil==(fila+1):
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and fil>(fila+1):

                
                if ModoProsperar == True:
                 entraste2 = True 
                 for l in range(fila+1,fil): #en la
                  if avisar2 == True:
                   for h in range(100):
                    for a in range(self.listaMuestras.tamaño()): 
                     for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                      if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and columna == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                       self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1
                  self.dot.node(f'{l},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar2 == True:
                   contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                   print("--------La muestra prosperará--------")
                   self.prosperará=True
                   self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar2 = False                  
                 break 
                else:
                 
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")
                 break
          if entraste2 == True:
           self.dot.render('Tablero',view=True)
        elif i ==3: #verificar arriba, fila restará hacia arriba
         entraste3=False
         fil1 = fila
         fil1 -= 1
         avisar3 = True
         if self.verificacionExiste(fila,columna) :  
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              if columna == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil1 :
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) :
                 fil1 -= 1 
                 if fil1 == (fila-1):
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and fil1 < (fila-1):

                
                if ModoProsperar == True: 
                 entraste3 = True
                 for l in range(fil1+1,fila): #en la
                   if avisar3 == True:
                    for h in range(100):
                     for a in range(self.listaMuestras.tamaño()): 
                      for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                       if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and columna == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                        self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1

                   self.dot.node(f'{l},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar3 == True:
                    contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                    print("--------La muestra prosperará--------")
                    self.prosperará=True
                    self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar3 = False                                  
                 break 
                else:
                 
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")
                 break
          if entraste3 == True:
           self.dot.render('Tablero',view=True)  

        elif i ==4: #verificar diagonal arriba derecha, fila restará hacia arriba y columna suma derecha
         entraste4=False
         fil1 = fila
         fil1 -= 1
         col1 = columna
         col1 +=1
         avisar4 = True
         if self.verificacionExiste(fila,columna) :  
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              if col1 == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil1 :
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 fil1 -= 1
                 col1 +=1 
                 if (fil1 == (fila-1) and col1 == (columna+1)):
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and (fil1 < (fila-1) and col1 > (columna+1)):
           
                if ModoProsperar == True :
                 entraste4 = True
                 for l in range(fil1+1,fila): #en la
                  for m in range(columna+1,col1): 
                   if avisar4 == True:
                    for h in range(100):
                     for a in range(self.listaMuestras.tamaño()): 
                      for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                       if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and m == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                        self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1

                   self.dot.node(f'{l},{m}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar4 == True:
                    contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                    print("--------La muestra prosperará--------")
                    self.prosperará=True
                    self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar4 = False                                  
                 break 
                else:
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled") 
                 break
          if entraste4 == True:
           self.dot.render('Tablero',view=True)  

        elif i ==5: #verificar diagonal arriba izquierda, fila restará hacia arriba y columna resta izquierda
         entraste5=False
         fil1 = fila
         fil1 -= 1
         col1 = columna
         col1 -=1
         avisar5 = True 
         if self.verificacionExiste(fila,columna) : 
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              if col1 == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil1 :
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 fil1 -= 1
                 col1 -=1 
                 if (fil1 == (fila-1) and col1 == (columna-1)):
                  break 
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and (fil1 < (fila-1) and col1 < (columna+1)):
      
                if ModoProsperar == True:
                 entraste5 = True
                 for l in range(fil1+1,fila): #en la
                  for m in range(col1+1,columna): 
                   if avisar5 == True:
                    for h in range(100):
                     for a in range(self.listaMuestras.tamaño()): 
                      for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                       if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and m == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                        self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1

                   self.dot.node(f'{l},{m}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar5 == True:
                    contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                    print("--------La muestra prosperará--------")
                    self.prosperará=True
                    self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar5 = False                                  
                 break
                else:
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")  
                 break
          if entraste5 == True:
           self.dot.render('Tablero',view=True)   

        elif i ==6: #verificar diagonal abajo izquierda, fila sumará hacia abajo y columna resta izquierda
         entraste6=False
         fil1 = fila
         fil1 += 1
         col1 = columna
         col1 -=1
         avisar6 = True 
         if self.verificacionExiste(fila,columna) :
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              if col1 == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil1 :
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 fil1 += 1
                 col1 -=1 
                 if (fil1 == (fila+1) and col1 == (columna-1)):
                  break
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and (fil1 < (fila-1) and col1 > (columna+1)):
            
                if ModoProsperar == True: 
                 entraste6 = True
                 for l in range(fila+1,fil1): #en la
                  for m in range(col1+1,columna): 
                   if avisar6 == True:
                    for h in range(100):
                     for a in range(self.listaMuestras.tamaño()): 
                      for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                       if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and m == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                        self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1

                   self.dot.node(f'{l},{m}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar6 == True:
                    contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                    print("--------La muestra prosperará--------")
                    self.prosperará=True
                    self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar6 = False                                  
                 break  
                else:
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")
                 break
          if entraste6 == True:
           self.dot.render('Tablero',view=True)   

        elif i ==7: #verificar diagonal abajo derecha, fila sumará hacia abajo y columna suma a la derecha
         entraste7=False
         fil1 = fila
         fil1 += 1
         col1 = columna
         col1 +=1
         avisar7 = True
         if self.verificacionExiste(fila,columna) :  
          for n in range(1000):
            for j in range(self.listaMuestras.tamaño()): 
             for k in range(self.listaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
              if col1 == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna) and int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila) == fil1 :
               if (ncodigo+1) != int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo):
                 fil1 += 1
                 col1 +=1 
                 if (fil1 == (fila+1) and col1 == (columna+1)):
                  break
               elif (ncodigo+1) == int(self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo) and (fil1 > (fila+1) and col1 > (columna+1)):
                
                if ModoProsperar == True:
                 entraste7 = True 
                 for l in range(fila+1,fil1): #en la
                  for m in range(columna+1,col1): 
                   if avisar7 == True:
                    for h in range(100):
                     for a in range(self.listaMuestras.tamaño()): 
                      for b in range(self.listaMuestras.invocar(a).ListaCeldasVivas.tamaño()):
                     
                       if l == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).fila) and m == int(self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).columna):
                        self.listaMuestras.invocar(a).ListaCeldasVivas.invocar(b).codigoOrganismo = ncodigo+1

                   self.dot.node(f'{l},{m}',shape = "square",width = '0.1', height= '0.1',fillcolor=codigo,style ="filled")                 
                 if avisar7 == True:
                    contener1 = CeldaViva(fila,columna,self.listaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                    print("--------La muestra prosperará--------")
                    self.prosperará=True
                    self.listaMuestras.invocar(j).ListaCeldasVivas.AgregarCabeza(contener1)
                 avisar7 = False                                  
                 break
                else:
                 self.dot.node(f'{fila},{columna}',shape = "square",width = '0.1', height= '0.1',fillcolor='grey',style ="filled")
                 break
          if entraste7 == True:
           self.dot.render('Tablero',view=True)
       if self.prosperará == False:
        if ModoProsperar == True: 
         print("--------La muestra no prosperará y muere, ó ya hay una muestra aqui--------")
          