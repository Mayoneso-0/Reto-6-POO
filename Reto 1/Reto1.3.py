# Escribir una función que reciba una lista de números y devuelva solo aquellos
#  que son primos. La función debe recibir una lista de enteros y retornar solo
#  aquellos que sean primos.

# Definicion de variables
lista_string = ""
lista = []
lista_primos = []

# Definicion de la funcion que verifica si un numero es primo
def es_primo(num):
    if num > 2:
        for i in range(2,num-1):
            if num % i == 0:
                return False
        return True
    elif num == 2:
        return True
    else:
        return False

try:
    # Pide una lista de numeros
    lista_string = input("Ingrese una lista de numeros: ")

    # Separa los numeros por espacios y los convierte a enteros
    lista_string = lista_string.split(" ")
    for i in range(len(lista_string)):
        lista.append(int(lista_string[i]))

    # Separa los numeros primos de la lista
    for i in range(len(lista)):
        if es_primo(lista[i]):
            lista_primos.append(lista[i])

    # Imprime la lista de numeros primos
    print("La lista de numeros primos es: ", lista_primos)
except ValueError:
    print("Error: Ingrese solo números enteros separados por espacios.")
except Exception as error:
    print(f"Error inesperado: {error}")


