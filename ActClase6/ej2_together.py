import math as m

def area():
    a = float(input("Ingrese el valor a: "))
    b = float(input("Ingrese el valor b: "))
    c = float(input("Ingrese el valor c: "))
 
    s = (a + b + c) / 2

    area = m.sqrt(s*(s-a)*(s-b)*(s-c))

    #print("area: ", area, "m2")

    return area
    #otorga el valor de una función

if __name__ == "__main__":
    print("area:",area(),"m2")