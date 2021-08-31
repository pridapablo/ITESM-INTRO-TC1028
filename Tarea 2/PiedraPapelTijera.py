# piedra papel o tijera
def ppot():
    ana = str(input("Tirada de Ana: "))
    juan = str(input("Tirada de Juan: "))

    #  piedra = "a"
    #  papel = "p"
    #  tijera = "t"

    if len(ana) > 1:
        return "Las tiradas deben de ser un caracter"

    elif len(juan) > 1:
        return "Las tiradas deben de ser un caracter" 
        
    elif (ana == "a" and juan == "t"):
        return "Gana Ana"
    
    elif (ana == "t" and juan == "p"):
        return "Gana Ana"

    elif (ana == "p" and juan == "a"):
        return "Gana Ana"

    elif (juan == "a" and ana == "t"):
        return "Gana Juan"
    
    elif (juan == "t" and ana == "p"):
        return "Gana Juan"

    elif (juan == "p" and ana == "a"):
        return "Gana Juan"

    elif (ana == juan) and ana == ("a" or "p" or "t"):
        return "Empate"   

    else:
        return "Tirada incorrecta"

if __name__ == "__main__":
    ret = ppot()
    print(ret)