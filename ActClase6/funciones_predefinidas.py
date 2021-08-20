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
    # range hace un rango entre cero y 5
    #secuencia de números hasta el anterior del número que pones entre paréntesis
    print(list(x))
    #list convierte de cadena de valores numéricos a una lista
    y = [3,5,9]
    print(max(y))
    print(min(y))
    #imprime el más chico o el más grande de una lista de números (guardados en la variable y)

if __name__ == "__main__":
    cadenas()
    números()