personas = ["Pedro", "Carla", "Laura", "José", "Marta"]

calorias = {
    "Pedro": (2000, 1800, 2100, 2000, 1900, 2500, 2200),
    "Carla": (1500, 1600, 1700, 1550, 1500, 1800, 1900),
    "Laura": (2500, 2600, 2400, 2300, 2400, 2500, 2600),
    "José": (1800, 1900, 2000, 2100, 2000, 1900, 1800),
    "Marta": (1300, 1400, 1350, 1250, 1200, 1500, 1600)
}

for persona, consumo in calorias.items():
    promedio = sum(consumo) / len(consumo)

    if promedio > 2000:
        print(f"{persona} tiene consumo alto")
    else:
        print(f"{persona} tiene consumo dentro del rango recomendado")
