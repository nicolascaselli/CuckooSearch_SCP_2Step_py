from   datetime import datetime
from   glob     import glob
import os

def SelectMandatory(Constrains, MaxVariables, DirOutput):
    Mandatory = []
    for Punt in range(MaxVariables):
        Mandatory.append(0)
    for Row in range(len(Constrains)):
        if len(Constrains[Row]) == 1:
            Mandatory[Constrains[Row][0]] = 1
    print(Mandatory, file = open(DirOutput + "MANDATORY.TXT", "w"))
    return Mandatory

def CreateRestricciones(Constrains, MaxVariables):
    """Método que toma las restricciones de la instancia y crea la matriz correspondiente para tratarla
    """
    Restricciones = []
    for Row in range(len(Constrains)):
        Restricciones.append([])
        for Col in range(MaxVariables):
            Restricciones[Row].append(0)
    for Row in range(len(Constrains)):
        for Col in range(len(Constrains[Row])):
            Restricciones[Row][Constrains[Row][Col]] = 1
    return Restricciones  
#------------------------------------------------------------------------------
def Cronometro(Inicio):
    Fin = datetime.now()
    Tiempo = Fin - Inicio
    Tiempo = str(Tiempo)
    Punto  = Tiempo.find(".")
    return Tiempo[0:Punto]
#------------------------------------------------------------------------------
def GetBestKnown(Instancia):    
    print("Leyendo Best Known...")    
    Instancia = Instancia.upper().replace("INPUT\\","")
    Archivo = open("Input/BestInstance.csv","r")
    Registro = Archivo.readline()
    while Registro != "":
        Campos = Registro.split(";")
        #print(Campos[0].upper(),Instancia)
        #input()
        if Campos[0].upper() == Instancia:
            return int(Campos[1])
        Registro = Archivo.readline()
    input("Se ha encontrado un error al leer la instancia: " + Instancia)
    return 0        
#------------------------------------------------------------------------------
def CreateDirectory(Instancia):  
    print("Creando estructura de carpetas...")          
    Instancia         = Instancia.replace("INPUT\\","").upper()
    Instancia         = Instancia.replace(".TXT","")
    #FileOutput        = Instancia + " " + time.strftime("%y%m%d %H%M")
    
    DirOutput         = "OUTPUT" # + Instancia #+ "/"
    #try:
    #    os.stat(DirOutput)
    #except:
    #    os.mkdir(DirOutput)
        
    DirOutput = DirOutput + "/" + Instancia + " - "
    
    for Archivo in glob(DirOutput + "*.TXT"):
        os.remove(Archivo)
        
    return Instancia, DirOutput
#------------------------------------------------------------------------------
def SaveInstance(Cost, Constrains, Restricciones, Coverage, DirOutput, Version):
    print("Guardando Datos...") 
    if Version == 0:
        Version = "-NR"
    else:
        Version = ""
        
    print(Cost, file = open(DirOutput + "COST" + Version + ".TXT"     , "w"))

    for Row in range(len(Constrains)):
        print(Constrains[Row], file = open(DirOutput + "CONSTRAINS" + Version + ".TXT","a"))
    
    for Row in range(len(Restricciones)):
        print(Restricciones[Row], file = open(DirOutput + "RESTRICCIONES" + Version + ".TXT","a")) 
        
    for Row in range(len(Coverage)):
        print(Coverage[Row], file = open(DirOutput + "COVERAGE" + Version + ".TXT","a"))   
    return None
#------------------------------------------------------------------------------
def ListadoInstancias(path, filtro):
    spath = path + filtro
    return glob(spath)  
#------------------------------------------------------------------------------
def ReadInstancia(Instancia):          
    print("Leyendo Instancia...") 
    Archivo       = open(Instancia, "r")
        
    # Leer Dimensión
    Registro           = Archivo.readline().split()
    TotalRestricciones = int(Registro[0])
    TotalVariables     = int(Registro[1])
    
    # Leer Costo
    Cost          = []
    Registro      = Archivo.readline()
    ContVariables = 1
    while Registro != "" and ContVariables <= TotalVariables:
        Valores = Registro.split()
        for Contador in range(len(Valores)):
            Cost.append(int(Valores[Contador]))
            ContVariables = ContVariables + 1
        Registro = Archivo.readline()
    
    # Preparar Matriz de Restricciones.
    Restricciones = []
    for Fila in range(TotalRestricciones):
        Restricciones.append([])
        for Columna in range(TotalVariables):
            Restricciones[Fila].append(0)
            
    # Leer Restricciones 
    Constrains    = []
    ContVariables = 1
    Fila          = 0
    while Registro != "":
        CantidadValoresUno = int(Registro)
        ContadorValoresUno = 0
        Registro = Archivo.readline()
        Constrains.append([])
        while Registro != "" and ContadorValoresUno < CantidadValoresUno: 
            Columnas = Registro.split()
            for Contador in range(len(Columnas)):
                Constrains[len(Constrains)-1].append(int(Columnas[Contador]) - 1)
                ContadorValoresUno = ContadorValoresUno + 1
            Registro = Archivo.readline()
        Fila = Fila + 1
    Archivo.close()
    
    # Obtener Cobertura para cada variable.
    Coverage = []
    for Col in range(len(Cost)):
        Coverage.append([])
    
    for Row in range(len(Constrains)):
        for Col in range(len(Constrains[Row])):
            Coverage[Constrains[Row][Col]].append(Row)
            
    # Calcular Factor de Cambio.
#    Rate  = []
    Order = []
#    for Punt in range(len(Coverage)):
#        Rate.append(Cost[Punt] / Coverage[Punt])
#        Order.append(Punt)
    
    # Ordenar por Factor.
#    for Punt1 in range(len(Rate)):
#        for Punt2 in range(len(Rate)):
#            if Rate[Punt1] > Rate[Punt2]:
#                Aux          = Rate[Punt1]
#                Rate[Punt1]  = Rate[Punt2]
#                Rate[Punt2]  = Aux
#                Aux          = Order[Punt1]
#                Order[Punt1] = Order[Punt2]
#                Order[Punt2] = Aux
    
    return Cost, Constrains, Coverage, Order