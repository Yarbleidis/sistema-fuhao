# Sistema de control de ventas diarias para el restaurante

class SistemaVentas:
    def __init__(self):
        self.total_dia = 0.0
        self.total_mes = 0.0
        self.nombre_mes = ""
        self.dia_actual = 1

    def preguntar_si_no(self, texto):
        # Valida que solo ingresen 's' o 'n'
        while True:
            resp = input(texto).strip().lower()
            if resp in ['s', 'si', 'sí']:
                return True
            elif resp in ['n', 'no']:
                return False
            else:
                print("Error: Ingresa solo 's' (sí) o 'n' (no).")

    def pedir_mes(self):
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "setiembre", "octubre",
            "noviembre", "diciembre"
        ]
        while True:
            mes = input("Ingresa el mes actual: ").strip().lower()
            if mes in meses:
                return mes.capitalize()
            else:
                print("Error: Eso no es un mes válido. Vuelve a intentar.")

    def pedir_celular(self):
        while True:
            cel = input("Número de celular (9 dígitos y empieza con 9): ").strip()
            if cel.isdigit() and len(cel) == 9 and cel.startswith('9'):
                return cel
            else:
                print(" Error: Debe tener exactamente 9 dígitos y empezar con 9.")

    def iniciar(self):

        print("   SISTEMA DE VENTAS DIARIAS - RESTAURANTE")

        self.nombre_mes = self.pedir_mes()

        while True:
            print(f"\n----------------------------------------")
            print(f" DÍA {self.dia_actual} de {self.nombre_mes}")
            print(f"----------------------------------------")

            # Ciclo para registrar los clientes del día
            while True:
                print("\n--- Registrar Nuevo Comensal ---")
                cliente = input("Nombre completo del comensal: ").strip()
                celular = self.pedir_celular()

                subtotal_cuenta = 0.0
                agregando = True

                while agregando:
                    try:
                        precio = float(input("Precio del plato o producto (S/.): "))
                        cant = int(input("Cantidad: "))
                        actual = precio * cant

                        # Ver si pidió adicional
                        if self.preguntar_si_no("¿Pidió algún adicional? (s/n): "):
                            p_adic = float(input("Precio del adicional (S/.): "))
                            c_adic = int(input("Cantidad del adicional: "))
                            actual += (p_adic * c_adic)

                        subtotal_cuenta += actual
                    except ValueError:
                        print(" Error: Ingresa números válidos en precio y cantidad.")
                        continue

                    agregando = self.preguntar_si_no(
                        "¿Desea agregar otro plato/producto? (s/n): "
                    )

                print("\n--------- TICKET DE VENTA ---------")
                print(f"Cliente: {cliente}")
                print(f"Celular: {celular}")
                print(f"Total a pagar: S/. {subtotal_cuenta:.2f}")
                print("-----------------------------------")

                # Acumulamos al día
                self.total_dia += subtotal_cuenta

                # Preguntar si quiere registrar otra venta hoy
                otra = self.preguntar_si_no(
                    "\n¿Registrar otra venta para este día? (s/n): "
                )
                if not otra:
                    break

            # Cierre del día
            print(f"\n** REPORTE DEL DÍA {self.dia_actual} **")
            print(f"Total recaudado hoy: S/. {self.total_dia:.2f}")

            # Sumamos al mes
            self.total_mes += self.total_dia

            # ¿Fin de mes?
            fin_de_mes = self.preguntar_si_no("\n¿Es el fin del mes? (s/n): ")
            if fin_de_mes:
                print(f"\n=== REPORTE TOTAL DE {self.nombre_mes.upper()} ===")
                print(f"Monto acumulado en el mes: S/. {self.total_mes:.2f}")
                print("¡Fin del mes registrado con éxito! Saliendo...")
                break
            else:
                # Preguntar si desea pasar al día siguiente
                siguiente = self.preguntar_si_no(
                    "\n¿Desea pasar al siguiente día? (s/n): "
                )
                if not siguiente:
                    print("Saliendo del sistema. ¡Buen trabajo!")
                    break

                # Preparar los montos para el siguiente día
                self.total_dia = 0.0
                self.dia_actual += 1


# Función para conectar con el menú principal
def ejecutar():
    app = SistemaVentas()
    app.iniciar()


if __name__ == "__main__":
    ejecutar()