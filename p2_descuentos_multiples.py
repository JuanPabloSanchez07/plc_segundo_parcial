
def calcular_precio_final(precio, categoria, unidades):
  descuento = 0
  if categoria == 'A':
      descuento = 0.10
  elif categoria == 'B':
      descuento = 0.05
  elif categoria == 'C':
      descuento = 0.02

  if unidades > 10:
      descuento += 0.05

  precio_final = precio * (1 - descuento)
  return precio_final

precio = float(input("Ingrese el precio del producto: "))
categoria = input("Ingrese la categoría (A, B o C): ")
unidades = int(input("Ingrese el número de unidades compradas: "))

precio_final = calcular_precio_final(precio, categoria, unidades)
print(f"Precio final después de descuentos: ${precio_final:.2f}")
