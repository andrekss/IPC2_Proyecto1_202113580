from Tablero import *
from PaintOrganismos import * 
from CargaXml import *

Load = Cargar()
x = None
y= None
aviso = True
while aviso == True:
 aviso = True

 print("        ╔═════════════════════════╗")
 print("        ║     Menú Principal      ║")
 print("        ║   1) Cargar Archivo     ║")
 print("        ║   2) Generar Tablero    ║")
 print("        ║   3) Hacer experimento  ║")
 print("        ║   4) Terminar programa  ║")
 print("        ╚═════════════════════════╝")
 Entrada = int(input("ingrese una opción: -> "))

 if Entrada == 1:
    Load.CargarArchivo()
    print("\nCarga Exitosa\n")

 elif Entrada ==2:
    Tableroo = Tablero(0,0)
    Tableroo.actualizar(Load,True,True)
    x= Tableroo.xVisualizar
    y= Tableroo.yVisualizar
 elif Entrada ==3:
  Tableroo = Tablero(x,y)
  print("        ╔═════════════════════════╗")
  print("        ║     Menú Experimento    ║")
  print("        ║ 1) Celdas que prosperan ║")
  print("        ║ 2) Generar Experimento  ║")
  print("        ║ 3) Xml actualizado      ║")
  print("        ║ 4) regresar             ║")  
  print("        ╚═════════════════════════╝")

  entrada = int(input("ingrese una opción: -> "))
  if entrada ==1:
   
   code2 = input("Coloque el código del organismo donde prosperará: ")
   code1 = code2
   co1 = Load.CodigoToInt(code1)
   o1 = Load.ListaOrganismos.invocar(co1-1).codigo
   definitivo1 = Load.CodigoToInt(o1)   
   Tableroo.actualizar(Load,False,False)
   filaInicio = int(input("Introduzca la fila inicial de la muestra: "))
   filaFinal = int(input("Introduzca la fila final de la muestra: "))
   columnaInicial = int(input("Introduzca la columna inicial de la muestra: "))
   columnaFinal = int(input("Introduzca la columna final de la muestra: "))

   for i in range(filaInicio-1,filaFinal+2):
     for j in range(columnaInicial-1,columnaFinal+2):
       if Tableroo.Orgas.verificacionExiste(j,i):
        Tableroo.Orgas.Prosperar(i,j,Tableroo.Orgas.Colores.invocar(int(definitivo1)-1),int(definitivo1)-1,False)
      
   Tableroo.Orgas.dot.render('Tablero',view=True)
  elif entrada ==2:
   i = int(input("Introduzca la fila: "))
   j = int(input("Introduzca la columna: "))

   code = input("Coloque el código del organismo: ")
   co = Load.CodigoToInt(code)

   o = Load.ListaOrganismos.invocar(co-1).codigo
   definitivo = Load.CodigoToInt(o)

   Tableroo.actualizar(Load,False,False)
   Tableroo.Orgas.GenerarPrueba(i,j,Tableroo.Orgas.Colores.invocar(int(definitivo)-1),False)
   Tableroo.Orgas.Prosperar(i,j,Tableroo.Orgas.Colores.invocar(int(definitivo)-1),int(definitivo)-1,True)
  elif entrada == 3:
    Load.GenerarXMLActualizado()
    print("termine el programa y vuelva iniciarlo para usar el archivo actualizado")
  elif entrada == 4:
    aviso ==False
 elif Entrada == 4:
   print("Hasta pronto . . .")
   exit()  