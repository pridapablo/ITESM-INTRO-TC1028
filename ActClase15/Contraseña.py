def main():
    a = input("Ingresa la contraseña: ")
    b = input("Confirma la contraseña: ")
    cont = 1

    while a != b and cont <= 3:
        b = input("Confirma la contraseña: ")
        cont += 1
    
    if a == b:
        print("Contraseña confirmada con éxito") 
    else:
        print("Contraseña incorrecta")

if __name__ == "__main__":
    main()