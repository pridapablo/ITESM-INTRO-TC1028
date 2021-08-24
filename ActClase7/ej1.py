num = int(input("Dame un número: "))
if num%2 == 0 and num>0:
    print("El número es par positivo")
elif num%2 == 0 and num<0:
    print("El número es par negativo")
elif num%2 != 0 and num>0:
    print("El número es impar positivo")
elif num%2 != 0 and num<0:
    print("El número es impar negativo")

