# Sistema de Gestión de Ventas Diarias para Restaurante

class SistemaVentasRestaurante:
    def __init__(self):
        self.monto_diario = 0.0
        self.monto_mensual = 0.0
        self.mes_actual = ""
        self.dia_actual = 1

    def preguntar_si_no(self, mensaje):
        """Función auxiliar para validar que el usuario ingrese exclusivamente sí o no."""
        while True:
            respuesta = input(mensaje).strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print(" Error: Ingrese una respuesta válida ('s' para sí, 'n' para no).")

    def validar_mes(self):
        """Función auxiliar para validar que se ingrese estrictamente el nombre de un mes válido."""
        meses_validos = {
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "setiembre", "octubre",
            "noviembre", "diciembre"
        }
        while True:
            mes = input("Ingrese el mes actual (ej. Octubre): ").strip().lower()
            if mes in meses_validos:
                return mes.capitalize()
            else:
                print("Error: El texto ingresado no corresponde a un mes válido del año. Intente nuevamente.")

    def validar_celular(self):
        """Función auxiliar para validar que el celular tenga 9 dígitos y empiece con el número 9."""
        while True:
            celular = input("Ingrese el número de celular del comensal (9 dígitos, empieza con 9): ").strip()
            if celular.isdigit() and len(celular) == 9 and celular.startswith('9'):
                return celular
            else:
                print("Error: El número de celular debe contener exactamente 9 dígitos y empezar con el número 9.")

    def iniciar_sistema(self):
        print("\n=== SISTEMA DE GESTIÓN DE VENTAS DIARIAS ===")
        self.mes_actual = self.validar_mes()

        # Bucle general para los días del mes
        while True:
            print(f"\n========================================")
            print(f"       DÍA {self.dia_actual} - (Mes: {self.mes_actual})")
            print(f"========================================")

            # Bucle para registrar múltiples ventas dentro del mismo día
            while True:
                print(f"\n--- NUEVA VENTA ---")
                nombre_comensal = input("Ingrese el nombre completo del comensal: ").strip()
                celular_comensal = self.validar_celular()

                total_cuenta = 0.0
                agregando_platos = True

                while agregando_platos:
                    try:
                        precio_plato = float(input("Ingrese el precio del plato o producto: S/. "))
                        cantidad = int(input("Ingrese la cantidad: "))
                        subtotal = precio_plato * cantidad

                        # Preguntar si pidieron algún adicional con validación
                        if self.preguntar_si_no("¿Pidió algún adicional? (s/n): "):
                            precio_adicional = float(input("Ingrese el precio del adicional: S/. "))
                            cant_adicional = int(input("Ingrese la cantidad del adicional: "))
                            subtotal += precio_adicional * cant_adicional

                        total_cuenta += subtotal
                    except ValueError:
                        print(" Error: Por favor, ingrese valores numéricos válidos para el precio y cantidad.")
                        continue

                    # Preguntar si desea agregar otro plato con validación
                    agregando_platos = self.preguntar_si_no(
                        "¿Desea agregar otro plato/producto para este comensal? (s/n): "
                    )

                # Resumen de la venta actual
                print("\n--- RESUMEN DE LA VENTA ---")
                print(f"Comensal: {nombre_comensal}")
                print(f"Celular: {celular_comensal}")
                print(f"Monto total a pagar: S/. {total_cuenta:.2f}")

                # Sumar al monto progresivo diario
                self.monto_diario += total_cuenta

                # Preguntar si desea registrar otra venta en el día con validación
                otra_venta = self.preguntar_si_no("\n¿Desea registrar otra venta? (s/n): ")
                if not otra_venta:
                    break  # Sale del bucle de ventas del día para ir al cierre diario

            # --- FIN DEL DÍA ---
            print(f"\n** REPORTE DIARIO (Día {self.dia_actual}) **")
            print(f"Monto total acumulado del día: S/. {self.monto_diario:.2f}")

            # Sumar al monto progresivo mensual
            self.monto_mensual += self.monto_diario

            # Consultar si es fin del mes con validación
            fin_mes = self.preguntar_si_no("\n¿Es el fin del mes? (s/n): ")
            if fin_mes:
                print(f"\n** CONSOLIDADO MENSUAL ({self.mes_actual}) **")
                print(f"Monto total acumulado del mes: S/. {self.monto_mensual:.2f}")
                print("¡Fin del mes registrado con éxito! Saliendo del sistema.")
                break
            else:
                # Preparar para el siguiente día
                siguiente_dia = self.preguntar_si_no(
                    "\n¿Desea iniciar las ventas para el siguiente día? (s/n): "
                )
                if not siguiente_dia:
                    print("Saliendo del sistema. ¡Hasta luego!")
                    break

                self.monto_diario = 0.0
                self.dia_actual += 1


# Función para conectar con el menú principal
def ejecutar():
    sistema = SistemaVentasRestaurante()
    sistema.iniciar_sistema()


if __name__ == "__main__":
    ejecutar()