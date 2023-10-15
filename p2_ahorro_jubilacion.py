
def calcular_pago_mensual(FV, r, n, t):
    PMT = FV * (r / ((1 + r)**n - 1) / (1 + r)**t)
    return PMT

edad_actual = int(input("Ingrese su edad actual: "))
edad_jubilacion = int(input("Ingrese la edad de jubilación: "))
cantidad_deseada = float(input("Ingrese la cantidad deseada para la jubilación: "))
rendimiento_anual = float(input("Ingrese el rendimiento anual esperado (en decimales): "))

n = (edad_jubilacion - edad_actual) * 12
t = edad_jubilacion - edad_actual
r = rendimiento_anual / 12

pago_mensual = calcular_pago_mensual(cantidad_deseada, r, n, t)
print(f"Debería ahorrar ${pago_mensual:.2f} mensualmente para alcanzar su meta de jubilación.")
