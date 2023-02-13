from nodo import Nodo

class ListaSimple:
    IdIncrementable = 0
    validación = True
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def Agregar(self, valor):
       self.IdIncrementable +=1
       if self.validación==True:
            self.cabeza = Nodo(valor,self.IdIncrementable)
            self.cola=self.cabeza
       else: 
           newNodo = Nodo(valor,self.IdIncrementable) 
           self.cabeza.setDirection(newNodo)
           self.cabeza = newNodo 
       self.validación = False
   
    def recorrido (self):    
        newNod = self.cola
        while newNod != None:
            print(newNod.getDato()," y su id ",newNod.getId())
            newNod = newNod.getDirection()