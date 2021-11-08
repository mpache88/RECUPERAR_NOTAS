class Dispositivo:
  def __init__(self, NOMBRE, MARCA, UBICACION , IOS, IPV4, MASK):
    self.NOMBRE = NOMBRE
    self.MARCA= MARCA
    self.UBICACION = UBICACION
    self.IOS = IOS
    self.IPV4 = IPV4
    self.MASK= MASK
  def MyNetwork (self):
    print("El/La " + self.NOMBRE + " de la marca " + self.MARCA + " se encuentra ubicado en " + self.UBICACION + " con un sistema operativo " + self.IOS + " tiene la IPV4 " + self.IPV4 + " con mascara " + self.MASK + ".")

loc1 = Dispositivo("Laptop", "HP" , "Lima", "Windows 10", "192.168.18.5" , "255.255.255.0" )
loc1.MyNetwork()
loc2 = Dispositivo("Celular", "LG" , "Iquitos", "Android", "192.168.17.192" , "255.255.255.0" )
loc2.MyNetwork()
loc3 = Dispositivo("Tablet", "Apple" , "Arequipa", "MacOS", "192.168.16.80" , "255.255.255.0" )
loc3.MyNetwork()
loc4 = Dispositivo("SmartTV", "LG" , "Lima", "WINDOWS 10", "192.168.18.94" , "255.255.255.0" )
loc4.MyNetwork()
your_loc = Dispositivo("PC", "Lenovo" , "Trujillo", "WINDOWS 10", "192.168.19.35" , "255.255.255.0" )
your_loc.MyNetwork ()
