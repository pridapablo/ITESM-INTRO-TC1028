def main():
    n=int(input("Cantidad de elementos a ingresar: "))
    lista=[]

    while n < 0:
        print("Tu número es inválido, intenta de nuevo")
        n=int(input("Cantidad de elementos a ingresar: "))

    for i in range(n):
        num = int(input())
        if num >= 0 and num <= 10:
            lista.append(num)
        else:
            print("El último número ingresado no es una calificación del 0 al 10")
            print("Volviendo a iniciar la captura")
            print("----------------------------------------------------------------")
            main()

    if n>0:
        prom=(sum(lista)/n)
        maxim=max(lista)
        minim=min(lista)
    else:
        prom=0
        maxim=0
        minim=0
    
    print(lista)
    print(f"Promedio: {prom}")
    print(f"Calificación mas alta: {maxim} Calificación mas baja: {minim}")

if __name__ == '__main__':
    main()