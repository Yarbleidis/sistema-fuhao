# SISTEMA DE GESTIÓN DE PEDIDOS DELIVERY
def ejecutar():
    # Lista para almacenar el historial de pedidos procesados en la sesión
    historial_pedidos = []

    continuar = "si"

    while continuar == "si":
        print("\n================ CONFIGURACIÓN DEL PEDIDO ================")

        nombre = input("Ingrese el nombre completo del comensal: ")

        # 1. VALIDACIÓN: Cantidad de platos
        while True:
            try:
                cantidad_platos = int(input("¿Cuántos platos diferentes va a solicitar?: "))
                if cantidad_platos > 0:
                    break
                print(" El número de platos debe ser mayor a 0.")
            except ValueError:
                print(" Error: Debe ingresar un número entero.")

        lista_platos = []
        precio_comida = 0.0
        tiempo_total_cocina = 0  # Variable para acumular el tiempo de todos los platos

        # BUCLE INTERNO PARA PLATOS
        for item in range(1, cantidad_platos + 1):
            plato_nombre = input(f"\n -> Ingrese el nombre del plato {item}: ")

            # 2. VALIDACIÓN: Precio de cada plato individual
            while True:
                try:
                    plato_precio = float(input(f" -> Ingrese el precio del plato {item} (S/.): "))
                    if plato_precio >= 0:
                        break
                    print(" El precio no puede ser negativo.")
                except ValueError:
                    print(" Error: Debe ingresar un monto numérico válido.")

            # 3. VALIDACIÓN NUEVA: Tiempo de preparación por CADA plato individual
            while True:
                try:
                    plato_tiempo = int(input(f" -> Ingrese los minutos de preparación del plato {item}: "))
                    if plato_tiempo >= 0:
                        break
                    print(" El tiempo no puede ser negativo.")
                except ValueError:
                    print(" Error: Debe ingresar un número entero para los minutos.")

            lista_platos.append(plato_nombre)
            precio_comida += plato_precio
            tiempo_total_cocina += plato_tiempo

            # 4. VALIDACIÓN: Distancia en kilómetros
        while True:
            try:
                distancia = float(input("\nIngrese la distancia en kilómetros: "))
                if distancia >= 0:
                    break
                print(" La distancia no puede ser negativa.")
            except ValueError:
                print(" Error: Debe ingresar un número válido para los kilómetros.")

        # 5. VALIDACIÓN: Estado del tráfico
        while True:
            try:
                trafico = int(input("Ingrese el estado vial (1: Normal / 2: Pesado): "))
                if trafico == 1 or trafico == 2:
                    break
                print(" Opción inválida. Solo se permite 1 o 2.")
            except ValueError:
                print(" Error: Debe ingresar el número 1 o el número 2.")

        # PROCESO

        # Calcular tiempo de viaje base y evaluar tráfico
        tiempo_viaje = distancia * 4
        if trafico == 2:
            tiempo_viaje += 12
            estado_trafico = "Congestionado"
        else:
            estado_trafico = "Fluido"

        # El tiempo total ahora es la SUMA de los tiempos de todos los platos pedidos
        tiempo_total = tiempo_total_cocina

        # Calcular costo del delivery
        if distancia <= 3:
            costo_delivery = 5.0
        else:
            excedente = distancia - 3
            costo_delivery = 5.0 + (excedente * 1.00)

        total_pagar = precio_comida + costo_delivery

        # Control de calidad de despacho
        mensaje_calidad = "ALERTA: Usar empaque térmico" if tiempo_total > 40 else "Despacho estándar"

        # SALIDAS
        print("\n----- RESUMEN PREVIO DEL PEDIDO -----")
        print(f"Comensal: {nombre}")
        print(f"Platos solicitados: {', '.join(lista_platos)}")
        print(f"Subtotal Comida: S/. {round(precio_comida, 2)}")
        print(f"Tiempo Total de Preparación de la Comida (Suma): {tiempo_total} minutos")
        print(f"Estado del tráfico en ruta: {estado_trafico}")
        print(f"Monto Total a Pagar: S/. {round(total_pagar, 2)} (Delivery: S/. {round(costo_delivery, 2)})")
        print(f"Control de calidad: {mensaje_calidad}")
        print("-" * 40)

        #  CONFIRMACIÓN / CANCELACIÓN DEL DELIVERY
        print("\n[ESTADO DEL DELIVERY] ¿El cliente confirma la orden o solicita la cancelación?")
        print("1: Confirmar y Enviar")
        print("2: Cancelar Pedido")

        estado_orden = input("Seleccione el estado (1 o 2): ")
        while estado_orden not in ["1", "2"]:
            estado_orden = input("Opción inválida. Seleccione 1 o 2: ")

        # Diccionario para estructurar los datos del pedido actual
        pedido_actual = {
            "comensal": nombre,
            "platos": lista_platos,
            "total": total_pagar,
            "tiempo": tiempo_total
        }

        if estado_orden == "2":
            pedido_actual["estado"] = "CANCELADO"
            pedido_actual["total_final"] = 0.0
            print(f"\n  Pedido CANCELADO.")
        else:
            pedido_actual["estado"] = "DESPACHADO"
            pedido_actual["total_final"] = total_pagar
            print("\n  Pedido despachado con éxito a la cocina.")

        # Guardar el registro en nuestra estructura de datos (Historial)
        historial_pedidos.append(pedido_actual)

        # Bucle de validación para la salida general del programa
        while True:
            entrada = input("\n¿Desea ingresar otro pedido al sistema? (si/no): ").strip().lower()
            if entrada in ["si", "no"]:
                continuar = entrada
                break
            print(" Respuesta inválida. Por favor, escriba estrictamente 'si' o 'no'.")

    # ================= REPORTE FINAL DEL DELIVERY =================
    print("\n" + "=" * 20 + " CIERRE DE CAJA " + "=" * 20)
    pedidos_exitosos = 0
    pedidos_cancelados = 0
    ingresos_totales = 0.0

    for p in historial_pedidos:
        ingresos_totales += p["total_final"]
        if p["estado"] == "DESPACHADO":
            pedidos_exitosos += 1
        else:
            pedidos_cancelados += 1

    print(f"• Total de pedidos intentados: {len(historial_pedidos)}")
    print(f"• Pedidos Despachados con Éxito: {pedidos_exitosos}")
    print(f"• Pedidos Cancelados: {pedidos_cancelados}")
    print(f"• Ingresos Netos de la Sesión: S/. {round(ingresos_totales, 2)}")
    print("==========================================================================")
    print("Sistema apagado correctamente. Datos transferidos.")

