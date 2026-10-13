# ============================================
#  SISTEMA DE PEDIDOS - Fundamentos de Programación
# ============================================


#Leer_texto solicita un texto al usuario mediante un input() y utiliza strip() para eliminar los espacios en blanco.
#Después, emplea while para comprobar si la respuesta está vacía. Si lo está, muestra un mensaje de error y vuelve a
#solicitar el texto. Cuando se ingrese una respuesta no vacía, return devuelve el texto y termina la función.
def leer_texto(mensaje):
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: No puede estar vacío.")
        texto = input(mensaje).strip()
    return texto


#Leer_precio solicita un precio y válida que sea un número mayor que cero. Utiliza while para repetir la solicitud hasta
#obtener un dato válido. Try para que intente el código valor, if comprueba que el valor sea mayor que cero, y return
#devuelve el precio y termina la función. Si ocurre un ValueError, except captura el error y pass permite continuar sin
#ejecutar ninguna acción en ese bloque. Si el precio no es válido se muestra un mensaje de error
def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
        except ValueError:
            pass
        print("Error: Ingresa un numero mayor que 0.")


#Función leer_opción recibe un mensaje y una lista de opciones válidas. Input() para solicitar una respuesta, strip()
#para eliminar espacios al principio y final, y upper() para convertir a mayúsculas. Mediante while comprueba si la
#opción ingresada no pertenece a la lista de opciones válidas. Si no pertenece muestra un mensaje de error y vuelva a
#solicitar. Cuando se ingresa una opción válida, return devuelve la respuesta y termina la funcion.
def leer_opcion(mensaje, valida):
    opcion = input(mensaje).strip().upper()
    while opcion not in valida:
        print(f"Opción inválida. Elige entre: {'/'.join(valida)}")
        opcion = input(mensaje).strip().upper()
    return opcion


#Leer_celular solicita el número de celular y valída que tenga exactamente 9 dígitos y empiece con 9, como los celulares
#de Perú. Isdigit() comprueba que solo haya números, len() cuenta los caracteres y celular[0] es el primer dígito.
#While repite la solicitud hasta que el número cumpla las tres condiciones, y return devuelve el celular.
def leer_celular(mensaje):
    celular = input(mensaje).strip()
    while not (celular.isdigit() and len(celular) == 9 and celular[0] == "9"):
        print("Error: Ingresa un celular de 9 dígitos que empiece con 9.")
        celular = input(mensaje).strip()
    return celular


def ejecutar():
    print("\n=== MÓDULO DE GESTIÓN Y CÁLCULO DE PEDIDOS ===")


    cliente = leer_texto("Ingrese el nombre del cliente: ")
    celular = leer_celular("Ingrese el numero celular del cliente: ")

    #leer_texto llama a la funcion para validar que cliente no este vacío.

    print("\nTipo de pedido:")
    print("L = En local")
    print("P = Para llevar")
    print("D = Delivery")
    tipo = leer_opcion("Elige (L/P/D): ", ["L", "P", "D"])

    #Leer_opcion llama a la funcion, la cual recibe dos argumentos, el mensaje que se muestra, y la lista de respuestas
    #permitidas. En pocas palabras, mostramos los tipos de pedido, solicitamos una opcion válida, y guardamos en tipo.

    nombres_tipo = {
        "L": "Local",
        "P": "Para llevar",
        "D": "Delivery"
    }

    #Creamos un diccionario que relaciona cada letra del tipo de pedido con su nombre completo, para mostrarlo de forma
    #más clara más adelante.

    nombres = []
    precios = []
    cantidades = []
    subtotales = []

    #Creamos cuatro listas vacías para almacenar nombres, precios, cantidades, y subtotales de los productos
    #que el cliente vaya agregando.

    continuar = "S"
    while continuar == "S":
        print("\n--- Nuevo producto ---")
        nombre = leer_texto("Ingrese el nombre del producto: ")  #Leer_texto para evitar que quede vacío.
        precio = leer_precio("Ingrese el precio del producto (S/): ")  #Leer_precio se asegura que el precio sea mayor a 0.
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Error: Ingresa un numero mayor que 0.")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un numero entero.")

        nombres.append(nombre)  #Agregamos el valor de nombre a la lista de nombres.
        precios.append(precio)  #Agregamos el precio del producto a la lista precios.
        cantidades.append(cantidad)  #Cantidad se añade a la lista cantidades.
        subtotales.append(precio * cantidad)  #Multiplica el precio y cantidad, luego agrega resultado a la lista subtotales.

        continuar = leer_opcion("¿Agregar otro producto? (S/N): ", ["S", "N"])
        #Llamamos a leer_opcion para que el usuario responda S/N, y si responde otra cosa la función lo marca como error.
        #Repite el proceso hasta que el usuario marque N.



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
    #Mostramos los métodos disponibles, solicitamos una opción válida con leer_opción y guardamos
    #el método elegido para usarlo en cálculos posteriores.

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
    print(f"Tipo de pedido: {nombres_tipo[tipo]}") #Diccionario, si tipo contiene "D", nombres_tipo[tipo] devuelve
                                                   #Delivery. Asi muestra el nombre completo en lugar de la letra.
    print("-" * ancho)
    print(f"{'Producto': <20}{'Cant.': >6}{'P.Unit.': >11}{'Subtotal': >13}")

    #F-string permite usar instrucciones de formato(:<20y:>6). Se divide en tres: 'Producto' texto a imprimir, ":" indica
    #el comienzo del formato, y <20 alinea el texto a la izquierda dentro de un espacio de 20 caracteres.

    for i in range(len(nombres)):
        print(f"{nombres[i]:<20}{cantidades[i]:>6}{f'S/ {precios[i]:.2f}':>11}{f'S/ {subtotales[i]:.2f}':>13}")
        #El for recorre los productos, y el print muestra los datos: nombre de producto alineado <20 junto con su encabezado
        #Producto <20. Todos están alineados; Cant. >6 del encabezado con cantidades[i]: >6, etc.

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