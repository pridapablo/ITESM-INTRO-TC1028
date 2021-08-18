def main():
    naci = int(input("Dame el año de nacimiento: "))
    año = int(input("Dame el año actual: "))
    edad = año - naci
    #un año tiene .2 lustros 
    lustros = edad/5
    print("Los lustros que has vivido son:",lustros)


if __name__ == '__main__':
    main()