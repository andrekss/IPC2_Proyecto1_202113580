class Nodo:

    def __init__(self, dato, id):
        self.dato= dato
        self.id=id
        self.direction=None
    # getters y setters de dato y dirección  
    def getDato(self):
        return str(self.dato)

    def setDato(self, newValor):
        self.dato = newValor

    def getDirection(self):
        return self.direction

    def setDirection(self, newDirection):
        self.direction = newDirection
    def getId(self):
        return str(self.id)       