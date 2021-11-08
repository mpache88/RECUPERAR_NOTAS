#Analizar las direcciones IP de dispositivos de red en formato JSON
import json
import ipaddress 

with open('MYFILE.JSON','r') as file:
    data = json.load(file)
    print(data)