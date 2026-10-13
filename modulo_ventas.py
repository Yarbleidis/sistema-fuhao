# Sistema de Gestión de Ventas Diarias para Restaurante

class SistemaVentasRestaurante:
    def __init__(self):
        self.monto_diario = 0.0
        self.monto_mensual = 0.0
        self.mes_actual = ""
        self.dia_actual = 1

    def iniciar_sistema(self):
        print("=== SISTEMA DE GESTIÓN DE VENTAS DIARIAS ===")
        self.mes_actual = input("Ingrese el mes actual (ej. Octubre): ").strip()

        # Bucle general para los días del mes
        while True:
            print(f"\n========================================")
            print(f"       DÍA {self.dia_actual} - (Mes: {self.mes_actual})")
            print(f"========================================")

            # Bucle para registrar múltiples ventas dentro del mismo día
            while True:
                print(f"\n--- NUEVA VENTA ---")
                nombre_comensal = input("Ingrese el nombre completo del comensal: ").strip()
                celular_comensal = input("Ingrese el número de celular del comensal: ").strip()

                total_cuenta = 0.0
                agregando_platos = True
                while agregando_platos:
                    try:
                        precio_plato = float(input("Ingrese el precio del plato o producto: S/. "))
                        cantidad = int(input("Ingrese la cantidad: "))
                        subtotal = precio_plato * cantidad

                        # Preguntar si pidieron algún adicional (acepta s, si, sí)
                        while True:
                            tiene_adicional = input(
                                "¿Pidió algún adicional? (s/n): "
                            ).strip().lower()

                            if tiene_adicional in ["s", "si", "sí", "n", "no"]:
                                break

                            print("Respuesta inválida. Ingrese s/n o si/no.")

                        if tiene_adicional in ["s", "si", "sí"]:
                            precio_adicional = float(
                                input("Ingrese el precio del adicional: S/. ")
                            )
                            cant_adicional = int(
                                input("Ingrese la cantidad del adicional: ")
                            )
                            subtotal += precio_adicional * cant_adicional

                        total_cuenta += subtotal
                    except ValueError:
                        print("Por favor, ingrese valores numéricos válidos.")
                        continue

                    # Preguntar si desea agregar otro plato (acepta s, si, sí)
                    while True:
                        otro = input(
                            "¿Desea agregar otro plato/producto para este comensal? (s/n): "
                        ).strip().lower()

                        if otro in ["s", "si", "sí", "n", "no"]:
                            break

                        print("Respuesta inválida. Ingrese s/n o si/no.")

                    if otro in ["n", "no"]:
                        agregando_platos = False

                # Resumen de la venta actual
                print("\n--- RESUMEN DE LA VENTA ---")
                print(f"Comensal: {nombre_comensal}")
                print(f"Celular: {celular_comensal}")
                print(f"Monto total a pagar: S/. {total_cuenta:.2f}")

                # Sumar al monto progresivo diario
                self.monto_diario += total_cuenta

                # Preguntar si desea registrar otra venta en el día (acepta s, si, sí)
                while True:
                    otra_venta = input(
                        "\n¿Desea registrar otra venta? (s/n): "
                    ).strip().lower()

                    if otra_venta in ["s", "si", "sí", "n", "no"]:
                        break

                    print("Respuesta inválida. Ingrese s/n o si/no.")

                if otra_venta in ["n", "no"]:
                    break  # Termina el registro de ventas del día

            # --- FIN DEL DÍA ---
            print(f"\n** REPORTE DIARIO (Día {self.dia_actual}) **")
            print(f"Monto total acumulado del día: S/. {self.monto_diario:.2f}")

            # Sumar al monto progresivo mensual
            self.monto_mensual += self.monto_diario

            # Consultar si es fin del mes (acepta s, si, sí)
            while True:
                fin_mes = input(
                    "\n¿Es el fin del mes? (s/n): "
                ).strip().lower()

                if fin_mes in ["s", "si", "sí", "n", "no"]:
                    break

                print("Respuesta inválida. Ingrese s/n o si/no.")

            if fin_mes in ["s", "si", "sí"]:
                print(f"\n** CONSOLIDADO MENSUAL ({self.mes_actual}) **")
                print(f"Monto total acumulado del mes: S/. {self.monto_mensual:.2f}")
                print("¡Fin del mes registrado con éxito! Saliendo del sistema.")
                break
            else:
                # Preparar para el siguiente día
                self.monto_diario = 0.0
                self.dia_actual += 1

                siguiente_dia = input(
                    "\n¿Desea iniciar las ventas para el siguiente día? (s/n): "
                ).strip().lower()

                if siguiente_dia not in ["s", "si", "sí"]:
                    print("Saliendo del sistema. ¡Hasta luego!")
                    break



def ejecutar():
    sistema = SistemaVentasRestaurante()
    sistema.iniciar_sistema()


if __name__ == "__main__":
    ejecutar()