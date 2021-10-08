# Ciclos - Número al cuadrado mayor que N

# Escribe un programa que reciba un número entero y como resultado, debe encontrar el
# menor número tal que al elevarlo al cuadrado sea mayor que el número N dado por el usuario.

def main():

    cont = 1
    n = int(input("Escribe un número: "))

    while (cont ** 2) <= n:
        cont = cont + 1

    print(cont)

if __name__ == '__main__':
    main()