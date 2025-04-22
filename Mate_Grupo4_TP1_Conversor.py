#Conversión de Números:Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal. Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

#Conversor decimal a binario: 
################
###############
################




#Conversor binario a decimal :

#Se pide al usuario un input de ceros y unos (el input es str)

#variable CORTE para cerrar el ciclo si el usuario ya no quiere convertir mas numeros: 
CORTE = "*"
####Se comenta el print principal porque se probará el menú.###
#print (f"Ingrese un número binario  -formado por ceros y unos- . El programa lo convertirá a número decimal. Ingrese un {CORTE} para finalizar: ")
#Se le pide al usuario que ingrese un número binario, y se almacena en la variable num_usuario.
#num_usuario = (input())


# creamos una funcion para pasar de binario, a decimal, y luego la llamamos dentro del ciclo.
def binario_a_decimal(binario):
    #La función int(numerobinario,2) convierte el número binario a decimal.
    #El segundo parámetro indica la base del número que se está convirtiendo.
 
    if all(char in '01' for char in binario): #Est. condicional para validar que se ingresó realmente un número binario. 
        numero_decimal = int(binario, 2)
        print (f"El número binario {binario} equivale a {numero_decimal} en sistema decimal.")
        return numero_decimal
    else: 
         print("El número ingresado es inválido. Por favor, ingrese un número binario -conformado por ceros y unos")
#esta es una función para pasar de decimal a binario, opcionalmente se puede hacer sacando el % (modulo) y guardar el resto.
def decimal_a_binario(decimal):
    decimal = int(decimal) #convertimos el número a entero, por si el usuario ingresa un número decimal. La funcion bin() no acepta string, por eso lo convertimos a entero.
    #La función bin(decimal) convierte el número decimal a binario.
    numero_binario = bin(decimal)[2:] #el [2:] es para quitar el prefijo '0b' que indica que es un número binario.
    #Se agregaron los numeros a ingresados por el usuario.
    print (f"El número decimal {decimal} equivale a {numero_binario} en sistema binario.")
    return numero_binario

#ciclo While para permitir al usuario pedir la conversion de todos los numeros que quiera, hasta que presione un *
# Esta logica está siendo reutilizada dentro de cada funcion para convertir.
""" while num_usuario != CORTE:
    if num_usuario == CORTE: #Condicional para cerrar el ciclo si el usuario ya no quiere convertir mas numeros.
        print ("Gracias por usar el conversor de binario a decimal. Hasta luego.")
        break
    if all(char in '01' for char in num_usuario): #Est. condicional para validar que se ingresó realmente un número binario.
        num_decimal = binario_a_decimal(num_usuario) #llamamos a la funcion, pasando por parametro la variable que almacena el input del usuario.
        print (f"Ingrese otro número binario  -formado por ceros y unos-. El programa lo convertirá a número decimal. Pulse {CORTE} para finalizar: ")
        num_usuario = (input())
    else:
        print ("El número ingresado es inválido. Por favor, ingrese un número binario -conformado por ceros y unos-- o un * para finalizar.")
        num_usuario = (input()) """
#Conversor decimal a binario:



################
###############
################

#opcion 2: hacer nosotros manualmente-- tipo tomar el caracter de la posicion 0  y multiplicarlo por 2**0 y así sucesivamente??? O dejamos lo otro?
# # Yo creo que el otro está bien, podemos explicar de dónde lo sacamos, por ahi de gpt o copilot o documentacion.

#MENU PRINCIPAL CON OPCIONES:
CORTE = "*"
def menu():
 #Iniciamos opcionMain vacio para que se pueda ejecutar el while.   
 opcionMain = ""  
 # Permite seguir ejecutando el programa hasta que se ingrese *. 
 while opcionMain != CORTE:
    print ("Bienvenido al conversor de números binarios a decimales y decimal a binario. Seleccione una opción:")
    print ("1. Convertir de binario a decimal")
    print ("2. Convertir de decimal a binario")
    print (f" Presione * para salir del programa")
    opcionMain = input("Ingrese su opción: ")
    # Ejecutamos la opcion seleccionada. No hace falta convertir los numeros asi que usamos strings.
    if opcionMain == "1":
        binario = input("Ingrese un número binario -formado por ceros y unos: ")
        binario_a_decimal(binario)
    elif opcionMain == "2":
        num_decimal = input("Ingrese un número decimal:")
        decimal_a_binario(num_decimal)
    elif opcionMain == CORTE:
        print("Gracias por utilizar el conversor. Muchas gracias.")
    else:
        print("Opcion invalida, intente nuevamente.")
menu()