
def calcular_nutrientes_receta(ingredientes, cantidades, informacion_nutricional):
    total_nutrientes = {}
    for i in range(len(ingredientes)):
        ingrediente = ingredientes[i]
        cantidad = cantidades[i]
        nutricion_por_100g = informacion_nutricional[i]

        for nutriente, valor_por_100g in nutricion_por_100g.items():
            if nutriente in total_nutrientes:
                total_nutrientes[nutriente] += (cantidad / 100) * valor_por_100g
            else:
                total_nutrientes[nutriente] = (cantidad / 100) * valor_por_100g

    return total_nutrientes

ingredientes = ["harina", "azúcar", "huevos"]
cantidades = [200, 50, 3]
informacion_nutricional = [
    {"calorías": 364, "proteínas": 10, "grasas": 1, "carbohidratos": 75},
    {"calorías": 194, "proteínas": 0, "grasas": 0, "carbohidratos": 50},
    {"calorías": 150, "proteínas": 12, "grasas": 10, "carbohidratos": 1}
]

nutrientes_totales = calcular_nutrientes_receta(ingredientes, cantidades, informacion_nutricional)
print("Nutrientes totales en la receta:")
for nutriente, valor in nutrientes_totales.items():
    print(f"{nutriente}: {valor:.2f} gramos")
