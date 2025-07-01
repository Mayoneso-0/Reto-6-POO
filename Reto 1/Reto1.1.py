# Crear una función que realice operaciones básicas (suma, resta, multiplicación
# , división) entre dos números, según la elección del usuario, la forma de 
# entrada de la función será los dos operandos y el caracter usado para la 
# operación. entrada: (1,2,"+"), salida (3).

# Definicion de variables
num1 = 0
num2 = 0
operacion = ""

# Definicion de la funcion
def calculadora(num1, num2, operacion):
    try:
        if operacion == "+":
            return num1 + num2
        elif operacion == "-":
            return num1 - num2
        elif operacion == "*":
            return num1 * num2
        elif operacion == "/":
            if num2 == 0:
                return "Error: División por cero"
            return num1 / num2
        else:
            return "Operacion no valida"    
    except Exception as error:
        return f"Error: {error}"

# Solicitar datos al usuario
try:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese la operacion deseada (+, -, *, /): ")
    # Realizar la operacion y mostrar el resultado
    print("El resultado es: ", calculadora(num1, num2, operacion))
except ValueError:
    print("Error: Ingrese solo números enteros válidos.")
except Exception as error:
    print(f"Error inesperado: {error}")


