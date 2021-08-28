def sortcond():
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))


    if x > y and x > z:
        mayor = x
    elif y > x and y > z:
        mayor = y
    elif z > x and z > y:
        mayor = z

    if x < y and x < z:
        menor = x
    elif y < x and y < z:
        menor = y
    elif z < x and z < y:
        menor = z

    if x < mayor and x > menor:
        medio = x
    elif y < mayor and y > menor:
        medio = y
    elif z < mayor and z > menor:
        medio = z
    
    print(menor)
    print(medio)
    print(mayor)

if __name__ == "__main__":
    sortcond()