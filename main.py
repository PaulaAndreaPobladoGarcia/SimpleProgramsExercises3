tiempo_total = 0

while True:
    duracion_tramo = int(input("Duracion tramo: "))
    
    if duracion_tramo == 0:
        break
    
    tiempo_total += duracion_tramo

horas = tiempo_total // 60  
minutos = tiempo_total % 60  

print(f"Tiempo total de viaje: {horas}:{minutos:02d} horas")
