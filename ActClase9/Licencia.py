def licencia():
    Edad = int(input("Ingresa tu edad: "))
    Tiene_ID = input("¿Tienes identificación oficial? (S/N): ")

    if (Edad >= 18) and (Tiene_ID == ("S" or "N" or "s" or "n")):
        return "Trámite de licencia concedido"
    elif (Edad < 0) or (Tiene_ID != ("S" or "N" or "s" or "n")):
        return "Respuesta incorrecta"
    else:
        return "No cumples requisitos"

if __name__ == "__main__":
    lic = licencia()
    print(lic)