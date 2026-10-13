# ======================================
# MENÚ PRINCIPAL - CHIFA FU-HAO
# Fundamentos de Programación 1
# ======================================

#Import trae el código de otro archivo .py que está en la misma carpeta.
#Cada módulo es un archivo distinto hecho por un integrante del grupo.
#Más abajo se llama a la función ejecutar() de cada uno.

import modulo_pedidos
import modulo_ventas
import modulo_platos
import modulo_horarios
import modulo_delivery

#Leer_opcion recibe un mensaje y una lista de opciones válidas.
#While repite la solicitud hasta que la opción ingresada pertenezca a la lista, y return devuelve la respuesta.

def leer_opcion(mensaje, valida):
    opcion = input(mensaje).strip().upper()
    while opcion not in valida:
        print(f"Opción inválida. Elige entre: {'/'.join(valida)}")
        opcion = input(mensaje).strip().upper()
    return opcion

#Opcion inicia en vacío para que el while entre la primera vez.
#El menú se repite después de cada módulo, hasta que el usuario elija 6 (Salir).

opcion = ""
while opcion != "6":
    ancho = 50
    print("\n" + "=" * ancho)
    print("BIENVENIDOS AL CHIFA FU-HAO".center(ancho))
    print("=" * ancho)
    print("¿Qué desea hacer?")
    print("1 = Gestión y cálculo de pedidos")
    print("2 = Gestión de ventas diarias")
    print("3 = Análisis de platos más vendidos")
    print("4 = Gestión de horarios del personal")
    print("5 = Gestión de pedidos por delivery")
    print("6 = Salir")

    opcion = leer_opcion("Elige (1/2/3/4/5/6): ", ["1", "2", "3", "4", "5", "6"])

    # Según la opción elegida, se llama a la función ejecutar() del módulo correspondiente.
    #Cuando el módulo termina, el programa vuelve al inicio del while y muestra el menú otra vez.

    if opcion == "1":
        modulo_pedidos.ejecutar()
    elif opcion == "2":
        modulo_ventas.ejecutar()
    elif opcion == "3":
        modulo_platos.ejecutar()
    elif opcion == "4":
        modulo_horarios.ejecutar()
    elif opcion == "5":
        modulo_delivery.ejecutar()
    else:
        print("\nGracias por usar el sistema. ¡Hasta pronto!")