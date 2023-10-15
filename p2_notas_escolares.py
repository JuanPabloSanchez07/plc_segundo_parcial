
def estadisticas_notas(notas):
    promedio = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    aprobados = sum(1 for nota in notas if nota >= 60)
    reprobados = len(notas) - aprobados

    return promedio, nota_maxima, nota_minima, aprobados, reprobados

notas = [80, 95, 45, 60, 75, 55, 70]
promedio, nota_maxima, nota_minima, aprobados, reprobados = estadisticas_notas(notas)

print(f"Promedio de notas: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")
