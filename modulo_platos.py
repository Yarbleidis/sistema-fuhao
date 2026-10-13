
# ============================================
# SISTEMA DE ANALISIS DE PLATOS MAS VENDIDOS
# ============================================

def ejecutar():
    # Registrar todos los platos de la carta con ventas iniciales en cero
    ventas = {
        "Aeropuerto": 0,
        "Chi-Jau-Kay": 0,
        "Ti-Pa-Kay": 0,
        "Pollo Saltado": 0,
        "Arroz Chaufa": 0,
        "Tallarín Saltado": 0,
        "Wantán Frito": 0,
        "Sopa Wantán": 0,
        "Kam Lu Wantán": 0,
        "Pollo Tipakay": 0
    }

    continuar = "si"

    print("\n========================================")
    print(" ANALISIS DE PLATOS MAS VENDIDOS - FU-HAO")
    print("========================================")

    # Registrar las ventas de los platos
    while continuar == "si":

        print("\n----- CARTA DE PLATOS -----")

        platos = list(ventas.keys())

        for i in range(len(platos)):
            print(f"{i + 1}. {platos[i]}")

        # Validar la selección del plato
        while True:
            try:
                opcion = int(input("\nSeleccione el numero del plato: "))

                if opcion >= 1 and opcion <= len(platos):
                    break

                print("Error: Seleccione un numero de la carta.")

            except ValueError:
                print("Error: Debe ingresar un numero entero.")

        plato_seleccionado = platos[opcion - 1]

        # Validar la cantidad vendida
        while True:
            try:
                cantidad = int(
                    input("Ingrese la cantidad de unidades vendidas: ")
                )

                if cantidad > 0:
                    break

                print("Error: La cantidad debe ser mayor que cero.")

            except ValueError:
                print("Error: Ingrese una cantidad entera valida.")

        # Acumular las unidades vendidas del plato seleccionado
        ventas[plato_seleccionado] += cantidad

        print(
            f"Registro realizado: {plato_seleccionado} "
            f"tiene {ventas[plato_seleccionado]} unidades vendidas."
        )

        # Preguntar si se desea registrar otra venta
        while True:
            respuesta = input(
                "\n¿Desea registrar otra venta? (si/no): "
            ).strip().lower()

            if respuesta == "si" or respuesta == "no":
                continuar = respuesta
                break

            print("Error: Escriba si o no.")

    # Analizar los resultados, incluyendo los platos con cero ventas
    mayor_ventas = max(ventas.values())
    menor_ventas = min(ventas.values())

    print("\n========================================")
    print("       REPORTE DE VENTAS - FU-HAO")
    print("========================================")

    print("\n----- VENTAS DE CADA PLATO -----")

    for plato, cantidad in ventas.items():
        print(f"{plato}: {cantidad} unidades")

    # Mostrar todos los platos empatados con más ventas
    print("\n----- PLATO(S) MAS VENDIDO(S) -----")

    for plato, cantidad in ventas.items():
        if cantidad == mayor_ventas:
            print(f"{plato}: {cantidad} unidades")

    # Mostrar todos los platos empatados con menos ventas
    print("\n----- PLATO(S) MENOS VENDIDO(S) -----")

    for plato, cantidad in ventas.items():
        if cantidad == menor_ventas:
            print(f"{plato}: {cantidad} unidades")

    print("\n========================================")
    print("Analisis finalizado.")
    print("========================================")


if __name__ == "__main__":
    ejecutar()
