#punto circunferencia

import math as m

def pto():
    radio = float(input("Introduce el radio: "))
    x1 =  float(input("Introduce x1: "))
    x2 =  float(input("Introduce x2: "))
    y1 =  float(input("Introduce y1: "))
    y2 =  float(input("Introduce y2: "))

    distancia = m.sqrt(abs(((x1-x2)**2)-(y1-y2)**2))
    # distancia entre dos puntos: cambio en x^2 + cambio en y^2 

    if (distancia < radio):
        return "DENTRO"

    if (distancia > radio):
        return "FUERA"

    if (distancia == radio):
        return "SOBRE"

if __name__ == "__main__":
    punto = pto()
    print(punto)