class Hosts:
    def __init__(self, bits):
        self.bits = bits
    def hosts(self):
        hostsTotal = (2 ** self.bits) - 2
        return hostsTotal
    def printHosts(self):
        myHosts= self.hosts()
        print ("Total de Hosts disponibles " + " es " + str(myHosts))

# Calculando el total de Hosts de acuerdo a los bits.
hosts1 = Hosts(8)
hosts1.printHosts()
hosts2 = Hosts(9)
hosts2.printHosts()
hosts3 = Hosts(10)
hosts3.printHosts()
