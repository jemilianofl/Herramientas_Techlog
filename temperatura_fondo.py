# Programa que calcula la temperatura de fondo en funci n de la profundidad.

# Recibe la profundidad y sus unidades (metros o pies).
# Luego, la temperatura se calcula con la f r mula:
# (3 * profundidad / 100) * 9 / 5 + 32 + 75
# Finalmente, se imprime la temperatura de fondo en la profundidad.

profundidad = float(input("Ingresa la profundidad: "))
unidades_profundidad = input("Ingresa las unidades (M o FT): ").upper()

if unidades_profundidad == "FT":
    profundidad *= 0.3048

# Calcula la temperatura de fondo con la f r mula.
temperatura_fondo = ((3 * profundidad / 100) * 9 / 5 + 32) + 75

# Imprime la temperatura de fondo en la profundidad.
print(f"La temperatura de fondo es: {temperatura_fondo:.2f} {unidades_profundidad}")

