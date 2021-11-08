import ipaddress

network = ipaddress.IPv4Network("192.168.1.0/24")

print("Dirección de red de la red:", network.network_address)

print("Dirección Broadcast:", network.broadcast_address)

print("Máscara de red:", network.netmask)

print("Con máscara de red:", network.with_netmask)

print("Longitud del prefijo de red en bits:", network.prefixlen)

print("Número total de hosts en la red:", network.num_addresses)
