def main():
    numeros=[]

    n=input()

    while n != "*":
        numeros.append(int(n))
        n=input()

    pares=0
    impares=0

    for elemento in numeros:
        if elemento % 2 == 0:
            pares=pares+1
        else: impares=impares+1

    print(f"Cantidad de pares: {pares}")
    print(f"Cantidad de impares: {impares}")

if __name__ == "__main__":
    main()