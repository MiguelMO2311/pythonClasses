def validar_ip(ip: str) -> bool:
    # Dividir la IP en sus partes
    partes = ip.split('.')
    
    # Verificar que haya exactamente 4 partes
    if len(partes) != 4:
        return False
    
    for parte in partes:
        # Verificar que cada parte sea un número y esté en el rango de 0 a 255
        if not parte.isdigit() or not 0 <= int(parte) <= 255:
            return False
    
    return True

# Solicitar la IP al usuario
ip = input("Introduce una dirección IP: ")
if validar_ip(ip):
    print(f"La IP {ip} es válida.")
else:
    print(f"La IP {ip} no es válida.")
