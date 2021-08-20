def cadenas():
    print("Hola")
    #imprimir
    print(len("Hola mundo"))
    #te da un entero con la cantidad de caracteres de la cadena
    a = ("Hola esto va a ser una lista")
    print(a.split())
    #split separa la cadena de caracteres usando los espacios (la separa en palabras diferentes)

def números():
    x = range(5)
    #secuencia de números
    print(list(x))
    #list convierte de cadena de valores numéricos a una lista

if __name__ == "__main__":
    #cadenas()
    números()