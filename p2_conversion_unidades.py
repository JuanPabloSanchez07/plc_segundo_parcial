
def convertir_unidad(cantidad, unidad_origen, unidad_destino):
    if unidad_origen == 'millas' and unidad_destino == 'kilometros':
        resultado = cantidad * 1.60934
    elif unidad_origen == 'litros' and unidad_destino == 'galones':
        resultado = cantidad * 0.264172
    elif unidad_origen == 'fahrenheit' and unidad_destino == 'celsius':
        resultado = (cantidad - 32) * 5/9
    # Agrega más conversiones según sea necesario

    return resultado

cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen: ").lower()
unidad_destino = input("Ingrese la unidad de destino: ").lower()

resultado = convertir_unidad(cantidad, unidad_origen, unidad_destino)
print(f"{cantidad} {unidad_origen} es igual a {resultado} {unidad_destino}")
