#Codigo Hecho por: Lexer Iván Juarez Vargas el 1/11/2024
# El proyecto de este módulo consiste en la creación de dos programas distintos:
# Uno que lea la longitud de una frase y otro que encuentre el cuadrante en un plano cartesiano según los dígitos que introduzcas.

# Programa para leer la longitud de una palabra ingresada y decir si es correcta o no

# Lectura y verificación de la longitud de la palabra ingresada 
def verificar_palabra():
    palabra = input("Por favor ingrese una palabra que tenga más de 4 letras y menos de 8:\n")
    longitud = len(palabra)

    if longitud < 4:  # El programa evalúa si la palabra es menor que 4
        print("Te faltan letras. Tu palabra tiene " + str(longitud) + " letras.")
    elif longitud > 8:  # El programa evalúa si la palabra es mayor que 8
        print("Te sobran letras. Tu palabra tiene " + str(longitud) + " letras.")
    else:  # El programa considera correcta cualquier palabra con longitud de 4 a 8
        print("Tu palabra es correcta.")

# Programa que determina en qué cuadrante está la coordenada ingresada
def encontrar_cuadrante():
    print("Ingrese las coordenadas. Recuerde que el primer dígito es la X.\nEjemplo 2,4: x = 2, y = 4.")
    x = int(input("Ingresa el valor de x: "))
    y = int(input("Ingresa el valor de y: "))

    # Determinación del cuadrante  
    if x == 0 and y == 0:
        print("Origen")
    elif x == 0:
        print("Eje Y")
    elif y == 0:
        print("Eje X")
    elif x > 0 and y > 0:
        print("Cuadrante I")
    elif x < 0 and y > 0:
        print("Cuadrante II")
    elif x < 0 and y < 0:
        print("Cuadrante III")
    elif x > 0 and y < 0:
        print("Cuadrante IV")   

while True:
    # Menú de opciones 
    print("¡Bienvenido!\nSeleccione una opción:")
    print("1.- Verificar la longitud de una palabra")
    print("2.- Determinar cuadrante")
    print("3.- Salir")

    opc = int(input("Ingrese el número de opción: "))

    # Uso de match para ejecutar la opción seleccionada
    match opc:
        case 1:
            verificar_palabra()  # Llama a la función de verificación de palabra
            input("Presione Enter para continuar...")
        case 2:
            encontrar_cuadrante()  # Llama a la función de encontrar cuadrante
            input("Presione Enter para continuar...")
        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

