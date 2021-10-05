def main():
    i = 0
    c = 0
    while i < 1000:
        a = int(input("Ingresa un valor a sumar "))
        c = c + 1
        i = i + a

    print ("suma es", i)
    print ("cantidad de números es", c)

if __name__ == "__main__":
    main()