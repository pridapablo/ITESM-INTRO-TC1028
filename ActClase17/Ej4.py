def main():
    
    sum_pos = 0
    sum_neg = 0
    cont = 0

    for i in range(1,7):
        print("Número", i, end=": ")
        n = int(input())

        if n > 0:
            sum_pos = sum_pos + n
            cont = cont+1

        else:
            sum_neg = sum_neg + n

    print("Sumatoria de los negativos:", sum_neg)

    prom_pos = sum_pos/cont

    print("Promedio de los positivos: ", prom_pos)

if __name__ == "__main__":
    main()