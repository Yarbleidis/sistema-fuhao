# ============================================
#  SISTEMA DE PEDIDOS - Fundamentos de Programación
# ============================================



def leer_texto(mensaje):
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: No puede estar vacío.")
        texto = input(mensaje).strip()
    return texto



def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
        except ValueError:
            pass
        print("Error: Ingresa un numero mayor que 0.")



def leer_opcion(mensaje, valida):
    opcion = input(mensaje).strip().upper()
    while opcion not in valida:
        print(f"Opción inválida. Elige entre: {'/'.join(valida)}")
        opcion = input(mensaje).strip().upper()
    return opcion



def leer_celular(mensaje):
    celular = input(mensaje).strip()
    while not (celular.isdigit() and len(celular) == 9 and celular[0] == "9"):
        print("\nError: Ingresa un celular de 9 dígitos que empiece con 9.")
        celular = input(mensaje).strip()
    return celular


def ejecutar():
    print("\n=== MÓDULO DE GESTIÓN Y CÁLCULO DE PEDIDOS ===")


    cliente = leer_texto("Ingrese el nombre del cliente: ")
    celular = leer_celular("Ingrese el numero celular del cliente: ")


    print("\nTipo de pedido:")
    print("L = En local")
    print("P = Para llevar")
    print("D = Delivery")
    tipo = leer_opcion("Elige (L/P/D): ", ["L", "P", "D"])

    

    nombres_tipo = {
        "L": "Local",
        "P": "Para llevar",
        "D": "Delivery"
    }

    

    nombres = []
    precios = []
    cantidades = []
    subtotales = []

    

    continuar = "S"
    while continuar == "S":
        print("\n--- Nuevo producto ---")
        nombre = leer_texto("Ingrese el nombre del producto: ")  
        precio = leer_precio("Ingrese el precio del producto (S/): ")  
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Error: Ingresa un numero mayor que 0.")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un numero entero.")

        nombres.append(nombre)  
        precios.append(precio)  
        cantidades.append(cantidad)  
        subtotales.append(precio * cantidad) 

        continuar = leer_opcion("¿Agregar otro producto? (S/N): ", ["S", "N"])
        



    costo_delivery = 0
    if tipo == "D":
        tarifa_base = 5
        km_base = 3
        costo_km_extra = 1.0

        distancia = leer_precio("\nDistancia al domicilio del cliente (km): ")

        if distancia <= km_base:
            costo_delivery = tarifa_base
        else:
            km_extra = distancia - km_base
            costo_delivery = tarifa_base + km_extra * costo_km_extra


    print("\nMétodo de pago:")
    print("E = Efectivo")
    print("T = Tarjeta")
    metodo = leer_opcion("Elige (E/T): ", ["E", "T"])
    

    #=====CÁLCULOS=====
    subtotal_general = 0

    for s in subtotales: #Recorre los elementos de la lista subtotales. S representa el valor de lo que lee cada vuelta.
        subtotal_general += s #Suma cada subtotal al acumulador. For recorre la lista y acumula los valores.

    if subtotal_general >= 200:
        porcentaje = 15
    elif subtotal_general >= 100:
        porcentaje = 10
    else:
        porcentaje = 0

    descuento = subtotal_general * (porcentaje / 100)

    total = subtotal_general - descuento + costo_delivery

    monto_pagado = 0
    vuelto = 0

    if metodo == "E": #Si metodo es "T", el bloque se omite.
        monto_pagado = leer_precio("\nMonto con el que paga el cliente (S/): ")
        while monto_pagado < total: #While ya sabe cuando debe terminar, por eso no se usa break.
            print(f"El monto no es suficiente. El total es S/{total:.2f}")
            monto_pagado = leer_precio("Monto con el que paga el cliente (S/): ")

        vuelto = monto_pagado - total

    total_unidades = 0 #Cuenta unidades individuales, no la cantidad de productos diferentes.
    for i in range(len(nombres)):
        total_unidades += cantidades[i] #Si fueran tres productos, len(nombres) devuelve 3 y range sería (3), y genera las
                                        #posiciones 0, 1, 2.


    ancho = 50 #Controlar el ancho de la boleta
    print("\n" + "=" * ancho)
    print("BOLETA DE PEDIDO".center(ancho))
    print("=" * ancho)
    print(f"Cliente: {cliente}")
    print(f"Celular: {celular}")
    print(f"Tipo de pedido: {nombres_tipo[tipo]}") 
                                                   
    print("-" * ancho)
    print(f"{'Producto': <20}{'Cant.': >6}{'P.Unit.': >11}{'Subtotal': >13}")

    

    for i in range(len(nombres)):
        print(f"{nombres[i]:<20}{cantidades[i]:>6}{f'S/ {precios[i]:.2f}':>11}{f'S/ {subtotales[i]:.2f}':>13}")
        

    print("-" * ancho)
    print(f"{'Subtotal:':<30}{f'S/ {subtotal_general:.2f}':>20}")
    print(f"{f'Descuento ({porcentaje}%):':<30}{f'S/ {descuento:.2f}':>20}")
    if tipo == "D":
        print(f"{'Delivery:':<30}{f'S/ {costo_delivery:.2f}':>20}")
    print("-" * ancho)
    print(f"{'TOTAL A PAGAR:':<30}{f'S/ {total:.2f}':>20}")

    if metodo == "E":
        print(f"{'Pago (efectivo):':<30}{f'S/ {monto_pagado:.2f}':>20}")
        print(f"{'Vuelto:':<30}{f'S/ {vuelto:.2f}':>20}")
    else:
        print(f"{'Pago:':<30}{'Tarjeta':>20}")

    print("-" * ancho)
    print(f"Total de unidades: {total_unidades}")
    print("-" * ancho)
