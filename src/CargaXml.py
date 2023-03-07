from xml.etree.ElementTree import *
from xml.dom.minidom import parseString
from ListaSimple import *
from MainListas import *

class Cargar:
    
    def __init__(self):
        self.ListaOrganismos = ListaSimple()
        self.ListaMuestras = ListaSimple()       

    def CargarArchivo(self):
      #Ruta = "/Users/gmg/Desktop/usac 2023/ipc2/release proyecto1/IPC2_Proyecto1_202113580/datos.xml"
      Ruta = input('Escriba la ruta exacta del archivo: ')
      Arbol = parse(Ruta) #cargamos el archivo en la variable Arbol
      raiz = Arbol.getroot() #entramos a la raíz de todo el archivo que sería datosMarte
      self.indicesColores = ListaSimple()
      contador = 0
      for lista in raiz:  #verde
       if contador == 0: #1er lista
          for orga in lista: #gris
             codigo = orga.find('codigo').text 
             nombre = orga.find("nombre").text
             orgas = Organismo(codigo,nombre) 
             self.ListaOrganismos.AgregarCabeza(orgas)
       elif contador == 1:
          for muestra in lista: 
             codigoM = muestra.find("codigo").text
             descripcion = muestra.find("descripcion").text
             filas= muestra.find("filas").text
             columnas = muestra.find("columnas").text
             listaCeldasVivas = muestra.find("listadoCeldasVivas")
             ListaCeldasLife = ListaSimple()          
             for celdaViva in listaCeldasVivas:
                fila= celdaViva.find("fila").text
                columna = celdaViva.find("columna").text
                codigoOrganismo = celdaViva.find("codigoOrganismo").text
                self.cel = CeldaViva(fila,columna,codigoOrganismo)
                ListaCeldasLife.AgregarCabeza(self.cel)     
             muest = Muestra(codigoM,descripcion,filas,columnas,ListaCeldasLife)
             self.ListaMuestras.AgregarCabeza(muest)   
       contador +=1
      #verificaciones 
      print("Lista de organismos:") 
      for i in range(self.ListaOrganismos.tamaño()):
             print("\nCódigo: ",str(self.ListaOrganismos.invocar(i).codigo))
             print("Nombre: ",str(self.ListaOrganismos.invocar(i).nombre),"\n")
             self.indicesColores.AgregarCabeza(self.ListaOrganismos.invocar(i).codigo)

      print("Lista de muestras:")
      for j in range(self.ListaMuestras.tamaño()): # recorremos la lista de muestras
             print("\ncodigoM: ",str(self.ListaMuestras.invocar(j).codigoM))
             print("descripcion: ",str(self.ListaMuestras.invocar(j).descripcion))
             print("filas: ",str(self.ListaMuestras.invocar(j).filas))
             print("columnas: ",str(self.ListaMuestras.invocar(j).columnas))

             print("\nLista de celdas vivas:")
             for k in range(self.ListaMuestras.invocar(j).ListaCeldasVivas.tamaño()): #recorrermos celdas vivas
                 print("\n","fila: ",self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila)
                 print("columna: ",self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna)
                 print("codigoOrganismo: ",self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                 
             print("\n")

             for l in range(self.indicesColores.tamaño()):
                 for j in range(self.ListaMuestras.tamaño()):
                     for k in range(self.ListaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
                      if self.indicesColores.invocar(l) == self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo:
                         self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo = l+1  
             print("*********************************")
             for j in range(self.ListaMuestras.tamaño()):
                for k in range(self.ListaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
                 print("codigoOrganismo: ",self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)

    
    def CodigoToInt(self,code):
      for i in range(self.ListaOrganismos.tamaño()):
                   if code == self.ListaOrganismos.invocar(i).codigo:
                      return int(i+1)
      return None   
                
    def GenerarXMLActualizado(self):
        raiz = Element('datosMarte')

        listaOrganismos = SubElement(raiz,'listaOrganismos')
        for i in range(self.ListaOrganismos.tamaño()):   
          Organismo = SubElement(listaOrganismos,'organismo')
          codigo = SubElement(Organismo, 'codigo')
          codigo.text = self.ListaOrganismos.invocar(i).codigo
          nombre = SubElement(Organismo, 'nombre')
          nombre.text = self.ListaOrganismos.invocar(i).nombre
        

        listaMuestras = SubElement(raiz,'listadoMuestras')  
        for j in range(self.ListaMuestras.tamaño()):
            Muestra = SubElement(listaMuestras,'muestra')
            codigoM = SubElement(Muestra,'codigo')
            codigoM.text = self.ListaMuestras.invocar(j).codigoM
            summary = SubElement(Muestra,'descripcion')
            summary.text = self.ListaMuestras.invocar(j).descripcion
            filas = SubElement(Muestra,'filas')
            filas.text = self.ListaMuestras.invocar(j).filas
            columnas = SubElement(Muestra,'columnas')
            columnas.text = self.ListaMuestras.invocar(j).columnas
        
            listaCelLife = SubElement(Muestra,'listadoCeldasVivas')
            for k in range(self.ListaMuestras.invocar(j).ListaCeldasVivas.tamaño()):
                celViva = SubElement(listaCelLife,'celdaViva')
                fila = SubElement(celViva,'fila')
                fila.text = str(self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).fila)
                columna = SubElement(celViva,'columna')
                columna.text = str(self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).columna)
                code = SubElement(celViva,'codigoOrganismo')
                code.text = str(self.ListaMuestras.invocar(j).ListaCeldasVivas.invocar(k).codigoOrganismo)
                

        xmlString = tostring(raiz, encoding="utf-8", xml_declaration=True) # Convierte el elemento raíz en un string XML con codificación UTF-8
        dom = parseString(xmlString) # Parsear el string XML a un objeto DOM para aplicar al formato
        xmlListo = dom.toprettyxml()  # Convierte el objeto DOM a un string ya mas legible 

        with open("datos(actualizados).xml", "w") as f: # Escribe el string con formato en el nuevo archivo'datos(actualizados).xml'
         f.write(xmlListo)
         