def licencia():
    Edad = int(input("Ingresa tu edad: "))
    
    if (Edad < 18):
        return "No cumples requisitos"
    else:
        Tiene_ID = str(input("¿Tienes identificación oficial? (s/n): "))

        if (Tiene_ID == "s"):
            return "Trámite de licencia concedido"
        elif (Tiene_ID == "n"):
            return "No cumples requisitos"
        else:
            return "Respuesta incorrecta"

if __name__ == "__main__":
    lic = licencia()
    print(lic)
