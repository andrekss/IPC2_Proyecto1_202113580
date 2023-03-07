class Organismo:
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre

class Muestra:

    def __init__(self,codigoM,descripcion, filas, columnas,ListaCeldasVivas):
        self.codigoM = codigoM
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas
        self.ListaCeldasVivas = ListaCeldasVivas

class CeldaViva:
    def __init__(self,fila,columna,codigoOrganismo):
        self.fila = fila
        self.columna = columna
        self.codigoOrganismo = codigoOrganismo        
