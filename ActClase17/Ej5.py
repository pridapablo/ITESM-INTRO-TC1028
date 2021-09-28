def main():
    inicial = int(input("Año inicial: "))
    final = int(input("Año final: "))

    for i in range(inicial,final):
        if (i % 4 == 0) and ((i % 100 != 0) or (i % 400 == 0)):
            print(i, end = " ")

if __name__ == "__main__":
    main()