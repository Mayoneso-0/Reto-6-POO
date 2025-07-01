# Realice una función que permita validar si una palabra es un palíndromo. 
# Condición: No se vale hacer slicing para invertir la palabra y verificar 
# que sea igual a la original.

palabra = ""
palindromo = False

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para evitar problemas
    palabra = palabra.lower()
    
    # Inicializar variables para el inicio y el final de la palabra
    inicio = 0
    fin = len(palabra) - 1
    
    # Recorrer la palabra desde ambos extremos hacia el centro
    while inicio < fin:
        if palabra[inicio] != palabra[fin]:
            return False
        inicio += 1
        fin -= 1
    
    return True

palabra = input("Ingrese una palabra: ")

try:
    if es_palindromo(palabra):
        print("La palabra es un palindromo.")
    else:
        print("La palabra no es un palindromo.")
except Exception as error:
    print(f"Error inesperado: {error}")

