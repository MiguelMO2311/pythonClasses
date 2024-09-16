semaforo_encendido = input("¿Está el semáforo encendido? (True/False): ").lower() == "true"
color_semaforo = input("Introduce el color del semáforo (verde, rojo, naranja): ").lower()

if semaforo_encendido:
    if color_semaforo == "verde":
        print("El semáforo está en verde")
    elif color_semaforo == "rojo":
        print("El semáforo está en rojo")
    elif color_semaforo == "naranja":
        print("El semáforo está en naranja")
    else:
        print("El semáforo está roto")
else:
    print("El semáforo está apagado")
