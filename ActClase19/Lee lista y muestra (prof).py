def main():
    n=int(input("Ingresa un número para el rango: "))
    lista=[]

    while n <= 0:
        print("Tu número es inválido, intenta de nuevo")
        n=int(input("Ingresa un número para el rango: "))

    for i in range(n):
        a = int(input())
        lista.append(a)

    cont=0

    for elemento in lista:
        print(f"lista[{cont}]={elemento}")
        cont = cont+1

    print(f"El último elemento es: {lista[-1]}")
    print(f"La suma de los elementos es: {sum(lista)}")
    print(f"El promedio de los elementos es: {sum(lista)/n}")

if __name__ == "__main__":
    main()