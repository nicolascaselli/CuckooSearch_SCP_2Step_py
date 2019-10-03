from cuckooSearch import cs
from scp import SCPTools as Tools

if __name__ == '__main__':
    print('Hello World')
    Instancias             = Tools.ListadoInstancias("INPUT/","M*.TXT")
    Semilla                = 2019
    for Instancia in Instancias: 
        Instancia, DirOutput                = Tools.CreateDirectory(Instancia)
        BestKnown                           = Tools.GetBestKnown(Instancia)        
        Cost, Constrains, Coverage, Order   = Tools.ReadInstancia("INPUT/" + Instancia + ".TXT")
        MaxVariables                        = len(Cost)
        Restricciones                       = Tools.CreateRestricciones(Constrains, MaxVariables)
        Mandatory                           = SelectMandatory(Constrains, MaxVariables, DirOutput)
        Tools.SaveInstance(Cost, Constrains, Restricciones, Coverage, DirOutput, 1)
        cs.run_CS()
    