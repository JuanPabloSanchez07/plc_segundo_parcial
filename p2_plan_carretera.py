
def calcular_costo_viaje(distancia, rendimiento, precio_gasolina, dias):
    costo_gasolina = (distancia / rendimiento) * precio_gasolina
    costo_total = costo_gasolina * dias
    return costo_total

distancia = float(input("Ingrese la distancia en millas: "))
rendimiento = float(input("Ingrese el rendimiento en millas por galón: "))
precio_gasolina = float(input("Ingrese el precio actual de la gasolina por galón: "))
dias = int(input("Ingrese cuántos días planea viajar: "))

costo_total = calcular_costo_viaje(distancia, rendimiento, precio_gasolina, dias)
print(f"El costo total del viaje será de ${costo_total:.2f}")
