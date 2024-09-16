#Descripción: Una empresa de transporte ofrece tarifas para el envío de paquetes con base en el peso y la distancia del envío. Las tarifas son las siguientes:
#Tarifa por peso:
#Hasta 1 kg: $10
#De 1 kg a 5 kg: $20
#Más de 5 kg: $30
#Tarifa por distancia:
#Hasta 100 km: $5
#De 101 km a 500 km: $15
#Más de 500 km: $25
#El cliente debe ingresar el peso del paquete y la distancia del envío. El programa debe calcular la tarifa total basándose en las tarifas por peso y distancia, y luego mostrar el costo total.

peso_paquete = float(input("Ingrese el peso del paquete en kg: "))
distancia_envio = float(input("Ingrese la distancia del envío en km: "))
if peso_paquete <= 1:
    tarifa_peso = 10
elif peso_paquete <= 5:
    tarifa_peso = 20
else:
    tarifa_peso = 30
if distancia_envio <= 100:
    tarifa_distancia = 5
elif distancia_envio <= 500:
    tarifa_distancia = 15
else:
    tarifa_distancia = 25
tarifa_total = tarifa_peso + tarifa_distancia
print(f"La tarifa total del envío es: ${tarifa_total}")