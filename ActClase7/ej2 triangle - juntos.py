def triangle():
    X = int(input("Lado 1: "))
    Y = int(input("Lado 2: "))
    Z = int(input("Lado 3: "))

    if (X>0  and Y>0 and Z>0) and (X + Y > Z) and (X + Z > Y) and (Y + Z > X):
        if X == Y and X == Z:
            return "el triángulo es equilatero"
        elif  X == Y or X == Z or Y == Z:
            return "el triángulo es isóceles"
        else:
            return "el triángulo es escaleno"
    else:
        return "X, Y y Z no son lados de un triángulo"

if __name__  == "__main__":
    triang = triangle()
    print(triang)
    #El resultado de return se guarda como si fuera una variable