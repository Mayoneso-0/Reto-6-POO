#Escribir una función que reciba una lista de string y retorne unicamente
#  aquellos elementos que tengan los mismos caracteres. 
# e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

# Definicion de variables
lista_original = ""
lista_string = []
lista_final = []

# Ingresa lista de palabras y la convierte a una lista de strings
try:
    lista_original = input("Ingrese una lista de palabras: ")
    lista_original = lista_original.split(" ")

    # Hace una copia de la lista original
    lista_string = lista_original.copy()

    # Separa los caracteres de cada palabra y los ordena
    for i in range(len(lista_string)):
        lista_string[i] = list(lista_string[i])
    for i in range(len(lista_string)):
        lista_string[i].sort()

    # Compara los caracteres de cada palabra con los de las otras palabras
    for i in range(len(lista_string)):
        for o in range(len(lista_string)):
            if lista_string[i] == lista_string[o] and i != o:
                lista_final.append(lista_original[i])
                break

    # Imprime la lista de palabras con los mismos caracteres
    print("La lista de palabras con los mismos caracteres es: ", lista_final)
except Exception as error:
    print(f"Error inesperado: {error}")