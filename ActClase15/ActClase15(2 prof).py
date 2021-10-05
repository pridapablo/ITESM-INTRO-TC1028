def main():
    
    suma = float(input("Dame un número inicial "))
    c = 1

    while suma <= 1000:
        num = float(input("Dame un número a sumar "))
        suma = suma + num

        c += 1

    print("La suma es", suma)
    print("Se sumaron", c, "números")

if __name__ == "__main__":
    main()