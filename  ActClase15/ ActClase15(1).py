def main():

    i = 0
    b = 1
    a = 2

    while b < a:
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))

        i = a

    while i <= b:
        if i % 2 == 0:
            print (i)    
        i = i+1

if __name__ == "__main__":
    main()