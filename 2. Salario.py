nombres_empleados = ["Juan", "Ana", "Luis", "Nadia", "Nico"]

horas_juan = (8, 8, 8, 8, 8, 0, 0)
horas_ana = (9, 9, 9, 9, 9, 4, 0)
horas_luis = (10, 10, 10, 10, 10, 8, 0)
horas_nadia = (7, 7, 7, 7, 7, 5, 0)
horas_nico = (5, 5, 5, 5, 5, 0, 0)

precio_hora = 375


# 1- Bucle for para recorrer la lista de empleados e imprimir cada nombre

for nombre in nombres_empleados:
    print(nombre)


# 2- Crear un diccionario con nombre como clave y horas como valor

diccionario = {
    "Juan": horas_juan,
    "Ana": horas_ana,
    "Luis": horas_luis,
    "Nadia": horas_nadia,
    "Nico": horas_nico
}

for a, b in diccionario.items():  # Imprimir el diccionario
    print(f"{a}: {b}")


# 3- Recorrer el diccionario e imprimir nombre y salario semanal
# 4- Condición para salario alto o bajo

for nombre, horas in diccionario.items():
    total_horas = sum(horas)
    salario = total_horas * precio_hora

    print(f"{nombre} gana ${salario} semanal")

    if salario > 18000:
        print(f"{nombre} tiene un salario alto")
    else:
        print(f"{nombre} tiene salario bajo")
