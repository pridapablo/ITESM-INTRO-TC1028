# Escribe un programa en el cual definas la función llamada calcula_grado. Esta función debe recibir 
# un número flotante entre 0 y 1, y debe regresar una nota alfabética de acuerdo con la siguiente tabla.

def calcula_grado(score):
    if score >= 0 and score <= 1:
        
        if score > 0.9:
            return "A"
        elif score > 0.8:
            return "B"
        elif score > 0.7:
            return "C"
        elif score > 0.6:
            return "D"
        elif score <= 0.6:
            return "F"

    else:
        return "Score incorrecto, debe ser un dato entre 0 y 1"

def main():
    grado = float(input("Ingresa el score: "))
    
    res = calcula_grado(grado)
    print(res)


if __name__ == "__main__":
    main()