# Alterna Caracteres
# Escribe un programa que lea un valor n y que muestre en la pantalla n caracteres que alternan entre # y %.
# Los caracteres se deben mostrar uno en cada renglón precedidos por el numero de renglón.
# El primer caracter que se debe mostrar siempre es #

def main():
    n = int(input())
    for i in range (1, n+1):
        if i % 2 != 0:
            print(str(i)+"-#")
        else:
            print(str(i)+"-%")


if __name__ == '__main__':
    main()