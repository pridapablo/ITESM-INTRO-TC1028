def main():
    n=int(input("Ingresa un número para el rango: "))
    lista=[]

    while n <= 0:
        print("Tu número es inválido, intenta de nuevo")
        n=int(input("Ingresa un número para el rango: "))

    for i in range(n):
        a = int(input())
        lista.append(a)

    for i in range(1,len(lista)):
        print(f"lista[{-i}]={lista[-i]}")

    print(f"El elemento más grande es: {max(lista)}")
    print(f"El elemento más pequeño es: {min(lista)}")
    print("El promedio de los elementos es: ",lista.sort())

if __name__ == "__main__":
    main()