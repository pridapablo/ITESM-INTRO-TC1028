def main():
    
    x = int(input('Introduce un número: '))
    
    if x>0 and x%2 == 0:
        return("El número es par positivo")
    elif x>0 and x%2 != 0:
        return("El número es impar positivo")
    elif x<0 and x%2 == 0:
        return("El número es par negativo")
    elif x<0 and x%2 != 0:
        return("El número es impar negativo")
    else:
        return("El 0 no es par ni impar")

if __name__ == '__main__':
    print(main())
