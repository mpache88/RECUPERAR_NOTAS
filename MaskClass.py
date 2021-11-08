class Prefijo:  
    def __init__(self, decimal):
        self.decimal= decimal
    def prefijo(self):
        PrefijoValue = bin(self.decimal) 
        return PrefijoValue
    def printPrefijo(self):
        myPrefijo = self.prefijo()
        print ( str(myPrefijo) + " Con este resultado se cuenta los 1 de los 2 ultimos octetos ")
        print ( " Por ultimo este resultado se le suma 16 bits y se obtiene el prefijo ")
# Calcular el prefijo mediante la máscara de subred.
prefijo1 = Prefijo(248)
prefijo1.printPrefijo()
prefijo2 = Prefijo(255)
prefijo2.printPrefijo()
prefijo3 = Prefijo(252)
prefijo3.printPrefijo()



