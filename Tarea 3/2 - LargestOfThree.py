# El programa va a preguntar por tres números, y al final debe imprimir sólo el número que es mayor que los demás.

# La salida del programa debe de ser exactamente de la siguiente forma:

# Enter first number: 6
# Enter second number: 9
# Enter third number: 4
# 9

def largest_of_three(a, b, c):
    if a > b and a > c:
        grande = a
    elif b > c and b > a:
        grande = b
    elif c > b and c > a:
        grande = c
    elif a == b and a == c:
        return "Los 3 números son iguales"

    return grande


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(largest_of_three(a, b, c))


if __name__ == '__main__':
    main()