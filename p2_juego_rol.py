
import random

def tirar_dado(dados, caras):
    resultado = sum(random.randint(1, caras) for _ in range(dados))
    return resultado

print("¡Bienvenido al juego de rol!")

personajes = ["Guerrero", "Mago", "Arquero"]
personaje_elegido = input("Elige un personaje (Guerrero, Mago, Arquero): ").capitalize()

if personaje_elegido in personajes:
    print(f"Has elegido ser un {personaje_elegido}.")

    # Aquí puedes agregar más lógica para enfrentar desafíos, tirar dados, etc.

else:
    print("Personaje no válido. Elige uno de los personajes disponibles.")
