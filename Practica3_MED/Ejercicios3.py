notas = []

for i in range(5):
    nota = float(input("Ingrese la nota número " + str(i + 1) + ": "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. Por favor, ingrese una nota entre 0 y 10.")

print("Notas ingresadas:", notas)
promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print("Nota media:", promedio)
print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
