X = int(input("ingresa longitud 1 "))
Y = int(input("ingresa longitud 2 "))
Z = int(input("ingresa longitud 3 "))

if (X>0  and Y>0 and Z>0) and (X + Y > Z) and (X + Z > Y) and (Y + Z > X):
    if X == Y and X == Z:
        print("el triángulo es equilatero")
    elif  X == Y or X == Z or Y == Z:
        print("el triángulo es isóceles")
    else:
        print("el triángulo es escaleno")
else:
    print("X, Y y Z no son lados de un triángulo")

