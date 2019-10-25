from    cuckooSearch    import cs
from cuckooSearch.config import Config as confCS
import time
from    glob            import glob
from    scp             import SCPTools
import os

if __name__ == '__main__':
    print(glob(os.path.join('input/'+ "m*.txt")))
    pathInstancias = os.path.join(os.getcwd(), 'input')
    pathResultados = os.path.join(os.getcwd(), 'output')
    #print("Extrayendo instancias desde el directorio:", pathInstancias)
    #print("Dejando resultados en el directorio:", pathResultados)
    
    #print(glob(os.listdir(os.path.join(os.getcwd(), 'input', "/M*.TXT"))))
    Instancias             = SCPTools.ListadoInstancias('input/',"m*.txt")
    #print(len(Instancias))
    for Instancia in Instancias: 
        print("ejecutando instancias")
        Instancia, DirOutput                = SCPTools.CreateDirectory(Instancia)
        BestKnown                           = SCPTools.GetBestKnown(Instancia)        
        Cost, Constrains, Coverage, Order   = SCPTools.ReadInstancia(os.path.join(pathInstancias , Instancia) + ".txt")
        MaxVariables                        = len(Cost)
        Restricciones                       = SCPTools.CreateRestricciones(Constrains, MaxVariables)
        Mandatory                           = SCPTools.SelectMandatory(Constrains, MaxVariables, DirOutput)
        SCPTools.SaveInstance(Cost, Constrains, Restricciones, Coverage, DirOutput, 1)
        print(Instancia)
        
        confCS.set_trial(1)
        confCS.set_iteration(2500)
        confCS.set_population_size(25)
        confCS.set_Cost(Cost)
        confCS.set_Restrictions(Restricciones)
        confCS.set_Constrains(Constrains)
        confCS.set_Mandatory(Mandatory)
        print("MAAXVARIABLES: ", MaxVariables)
        confCS.set_dimension(MaxVariables)
        cs.run_CS()
    