#Conversión de Números:Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal. Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

#Conversor decimal a binario: 
################
###############
################




#Conversor binario a decimal :

#Se pide al usuario un input de ceros y unos (el input es CADENA)

#variable CORTE para cerrar el ciclo si el usuario ya no quiere convertir mas numeros: 
CORTE = "*"
print ("Ingrese un número binario  -formado por ceros y unos- . El programa lo convertirá a número decimal. Ingrse un  ", CORTE, "para finalizar.")
num_usuario = (input())



#ciclo While para permitir al usuario pedir la conversion de todos los numeros que quiera, hasta que presione un *
while num_usuario != CORTE:
    if all(char in '01' for char in num_usuario): #Est. condicional para validar que se ingresó realmente un número binario.
        num_decimal = int(num_usuario,2) #Se usa la función int(numerobinario,2) para convertir el numero binario a decimal
        print ("El número binario ingresado equivale a ", num_decimal, "en sistema decimal.")
        print ("Ingrese un número binario  -formado por ceros y unos- . El programa lo convertirá a número decimal. Pulse ", CORTE, "para finalizar.")
        num_usuario = (input())
    else:
        print ("El número ingresado es inválido. Por favor, ingrese un número binario -conformado por ceros y unos-.")
        num_usuario = (input())
if ##### ACÁ PARA PONER , SI LA ENTRADA ES IGUAL AL ASTERISCO, ENTONCES CERRAR EL PROGRAMA DE CONVERSOR DE BINAROIS A DECIMALES. 



#opcion 2: hacer nosotros manualmente-- tipo tomar el caracter de la posicion 0  y multiplicarlo por 2**0 y así sucesivamente??? O dejamos lo otro?

