from   datetime import datetime
from   glob     import glob
import numpy as np
import os


def Binarizar(Probabilidades, Grupos, PopulationBin): 
    Puntero = 0
    for Row in range(len(PopulationBin)):
        for Col in range(len(PopulationBin[Row])):
            Posicion = Grupos.labels_[Puntero]
            if Posicion == -1 or Probabilidades[Posicion] > np.random.random():
                if PopulationBin[Row][Col] == 0:
                    PopulationBin[Row][Col] = 1
                else:
                    PopulationBin[Row][Col] = 0  
            Puntero += 1
    return PopulationBin

def BinarizarPoblacion2step(poblacion): 
    for Row in range(len(poblacion)):
        for Col in range(len(poblacion[Row])):
            if (poblacion[Row][Col] != 0) and (poblacion[Row][Col] != 1):
                if poblacion[Row][Col] >= 0.5 :
                    poblacion[Row][Col] = 1
                else:
                    poblacion[Row][Col] = 0

    return poblacion

def BinarizarSolucion2step(solucion): 
    for Col in range(len(solucion)):
            if solucion[Col] >= 0.5:
                solucion[Col] = 1
            else:
                solucion[Col] = 0
    return solucion
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
    Instancia = Instancia.upper().replace("INPUT/","")
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
    print("Creando estructura de carpetas...", Instancia)          
    Instancia         = Instancia.upper().replace("INPUT/","")
    Instancia         = Instancia.upper().replace(".TXT","")
    #FileOutput        = Instancia + " " + time.strftime("%y%m%d %H%M")
    
    DirOutput         = "OUTPUT" # + Instancia #+ "/"
    #try:
    #    os.stat(DirOutput)
    #except:
    #    os.mkdir(DirOutput)
        
    DirOutput = DirOutput + "/" + Instancia + " - "
    #print("carpeta de salida:", DirOutput)
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
    print(spath)
    return glob(spath)  
#------------------------------------------------------------------------------
def ReadInstancia(Instancia):
    """
    Lee lor archivos OR y genera las correspondiente variables con los costos, restricciones, covertura y orden
    Cost, Constrains, Coverage, Order
    """          
    print("Leyendo Instancia...", Instancia) 
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

def CumpleRestriccion(AgenteBin, Constrains):
    Cont = 0
    for Row in range(len(Constrains)):
        Col = 0
        while Col < len(Constrains[Row]):
            if AgenteBin[Constrains[Row][Col]] == 1:
                Cont += 1
                Col   = len(Constrains[Row])    
            Col += 1
    return Cont == len(Constrains)

def Quitar(AgenteBin, Mandatory, Constrains): 
    for Col in range(len(AgenteBin)-1,-1,-1):
        if AgenteBin[Col] == 1 and Mandatory[Col] == 0:
            AgenteBin[Col] = 0
            if not CumpleRestriccion(AgenteBin, Constrains):  
                AgenteBin[Col] = 1
    return AgenteBin
#------------------------------------------------------------------------------  

def QuitarExceso(PopulationBin, Mandatory, Constrains):
    for Row in range(len(PopulationBin)):
        PopulationBin[Row] = Quitar(PopulationBin[Row], Mandatory, Constrains)
    return PopulationBin

def FactibilizarAgente(solucion, Constrains): 
    for Row in range(len(Constrains)):
        Suma = 0
        for Col in range(len(Constrains[Row])):
            Suma += solucion[Constrains[Row][Col]]
        if Suma == 0:
            for Col in range(len(Constrains[Row])):
                if solucion[Constrains[Row][Col]] == 0:
                    solucion[Constrains[Row][Col]] = 1
                    break
    return solucion
#------------------------------------------------------------------------------  

def FactibilizaSolucion(solution, Constrains):
     
    if not CumpleRestriccion(solution, Constrains):            
            solution = FactibilizarAgente(solution, Constrains)
    return solution

def FactibilizaPoblacion(solution, Constrains):
    for Row in range(len(solution)):  
        if not CumpleRestriccion(solution[Row], Constrains):            
            solution[Row] = FactibilizarAgente(solution[Row], Constrains)
    return solution