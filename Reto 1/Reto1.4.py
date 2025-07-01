# Escribir una función que reciba una lista de números enteros y retorne la
#  mayor suma entre dos elementos consecutivos.

lista_string = ""
lista = []

try:
    lista_string = input("Ingrese una lista de numeros: ")
    # Separa los numeros por espacios y los convierte a enteros
    lista_string = lista_string.split(" ")
    for i in range(len(lista_string)):
        lista.append(int(lista_string[i]))

    # La mayor suma entre dos elementos consecutivos
    if len(lista) < 2:
        raise ValueError("Se requieren al menos dos números para calcular la suma de consecutivos.")
    mayor_suma = lista[0] + lista[1]
    mayor_posicion = [0,1]
    for i in range(len(lista)-1):
        if mayor_suma < lista[i] + lista[i+1]:
            mayor_suma = lista[i] + lista[i+1]
            mayor_posicion = [i,i+1]

    # Imprime la mayor suma entre dos elementos consecutivos y los elementos
    print("La mayor suma entre dos elementos consecutivos es: ", mayor_suma)
    print("Los elementos son: ",lista[mayor_posicion[0]],"y",lista[mayor_posicion[1]])
except ValueError as value_error:
    print(f"Error: {value_error}")
except Exception as error:
    print(f"Error inesperado: {error}")