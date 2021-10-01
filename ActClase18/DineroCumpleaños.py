def main():
    edad = int(input("Inserte la edad del niño: "))
    suma = 10

    while suma <= 1000:

        suma = suma * 2

        edad = edad + 1

    print(edad,"$"+str(suma))

if __name__ == "__main__":
    main()