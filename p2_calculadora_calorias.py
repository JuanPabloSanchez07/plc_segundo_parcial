
def calcular_calorias_quemadas(peso, duracion, actividad):
    if actividad == 'correr':
        calorias = 8.0 * duracion * peso
    elif actividad == 'nadar':
        calorias = 10.0 * duracion * peso
    elif actividad == 'andar en bicicleta':
        calorias = 4.0 * duracion * peso

    return calorias

peso = float(input("Ingrese su peso en kg: "))
duracion = int(input("Ingrese la duración en minutos: "))
actividad = input("Ingrese el tipo de actividad (correr, nadar, andar en bicicleta, etc.): ")

calorias_quemadas = calcular_calorias_quemadas(peso, duracion, actividad)
print(f"Calorías quemadas: {calorias_quemadas} cal.")
