# ============================================
# SISTEMA DE HORARIOS DEL CHIFA FU HAO
# ============================================

nombres = []
horas_entrada = []  # Turno programado de entrada
horas_salida = []  # Turno programado de salida
fechas_inicio = []

# Matriz / Lista de asistencias: [indice_trabajador, fecha, entrada_real, salida_real]
asistencias = []


def hora_a_segundos(hora_str):
    # Convierte "HH:MM:SS" a segundos totales para facilitar cálculos
    partes = hora_str.split(":")
    h = int(partes[0])
    m = int(partes[1])
    s = int(partes[2])
    return h * 3600 + m * 60 + s


def segundos_a_hora(segundos):
    # Convierte segundos totales de vuelta a formato "HH:MM:SS"
    signo = "-" if segundos < 0 else ""
    segundos = abs(segundos)
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{signo}{h:02}:{m:02}:{s:02}"


def mostrar_menu():
    print("\n--- SISTEMA DE ASISTENCIA Y HORAS ---")
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Registrar asistencia diaria (Entrada/Salida real)")
    print("4. Ver reporte de asistencias y balance de horas")
    print("5. Salir")


def registrar_trabajador():
    print("\n--- Registrar Trabajador ---")
    nombre = input("Ingrese el nombre del trabajador: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    entrada = input("Ingrese hora de entrada del turno (HH:MM:SS): ").strip()
    salida = input("Ingrese hora de salida del turno (HH:MM:SS): ").strip()
    inicio = input("Ingrese fecha de inicio (DD/MM/AAAA): ").strip()

    nombres.append(nombre)
    horas_entrada.append(entrada)
    horas_salida.append(salida)
    fechas_inicio.append(inicio)
    print("¡Trabajador registrado con éxito!")


def listar_trabajadores():
    print("\n--- Lista de Trabajadores ---")
    if len(nombres) == 0:
        print("No hay trabajadores registrados.")
        return

    i = 0
    while i < len(nombres):
        print(f"{i + 1}. {nombres[i]} | Turno: {horas_entrada[i]} - {horas_salida[i]}")
        i += 1


def registrar_asistencia():
    print("\n--- Registrar Asistencia Diaria ---")
    if len(nombres) == 0:
        print("No hay trabajadores registrados.")
        return

    listar_trabajadores()

    opcion_valida = False
    indice = 0
    while not opcion_valida:
        entrada_op = input("Seleccione el número del trabajador: ").strip()
        if entrada_op.isdigit():
            indice = int(entrada_op) - 1
            if 0 <= indice < len(nombres):
                opcion_valida = True
            else:
                print("Número fuera de rango.")
        else:
            print("Ingrese un número válido.")

    fecha = input("Ingrese la fecha de asistencia (DD/MM/AAAA): ").strip()
    entrada_real = input("Ingrese hora de entrada real (HH:MM:SS): ").strip()
    salida_real = input("Ingrese hora de salida real (HH:MM:SS): ").strip()

    # Guardar en la lista de asistencias
    asistencia_nueva = [indice, fecha, entrada_real, salida_real]
    asistencias.append(asistencia_nueva)
    print("¡Asistencia y marcajes registrados correctamente!")


def ver_asistencias():
    print("\n--- Reporte y Balance de Horas ---")
    if len(nombres) == 0:
        print("No hay trabajadores registrados.")
        return

    listar_trabajadores()

    opcion_valida = False
    indice = 0
    while not opcion_valida:
        entrada_op = input("Seleccione el número del trabajador: ").strip()
        if entrada_op.isdigit():
            indice = int(entrada_op) - 1
            if 0 <= indice < len(nombres):
                opcion_valida = True
            else:
                print("Número fuera de rango.")
        else:
            print("Ingrese un número válido.")

    nombre = nombres[indice]
    t_entrada = horas_entrada[indice]
    t_salida = horas_salida[indice]

    # Duración esperada del turno en segundos
    duracion_turno = hora_a_segundos(t_salida) - hora_a_segundos(t_entrada)
    if duracion_turno < 0:
        duracion_turno += 86400  # Manejo básico por si el turno cruza la medianoche

    print(f"\nReporte para: {nombre} | Turno programado: {t_entrada} a {t_salida}")
    encontrados = 0

    i = 0
    while i < len(asistencias):
        registro = asistencias[i]
        if registro[0] == indice:
            fecha = registro[1]
            e_real = registro[2]
            s_real = registro[3]

            # Duración real trabajada
            duracion_real = hora_a_segundos(s_real) - hora_a_segundos(e_real)
            if duracion_real < 0:
                duracion_real += 86400

            # Diferencia entre lo trabajado y lo programado
            diferencia = duracion_real - duracion_turno

            estado_balance = ""
            if diferencia > 0:
                estado_balance = f"Horas extra: {segundos_a_hora(diferencia)}"
            elif diferencia < 0:
                estado_balance = f"Debe horas: {segundos_a_hora(abs(diferencia))}"
            else:
                estado_balance = "Cumplió exactas las horas del turno"

            print(f"- Fecha: {fecha} | Entrada: {e_real} | Salida: {s_real} | {estado_balance}")
            encontrados += 1
        i += 1

    if encontrados == 0:
        print("No hay registros de asistencia para este trabajador.")


def ejecutar():
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            registrar_asistencia()
        elif opcion == "4":
            ver_asistencias()
        elif opcion == "5":
            print("Volviendo al menú principal del Chifa...")
            salir = True
        else:
            print("Opción inválida. Intente de nuevo.")
