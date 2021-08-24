import math as m

def distancia():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    x = x2-x1
    y = y2-y1

    distan = m.hypot(x,y)

    print("distancia="+str(round(distan,2)))

if __name__ == "__main__":
    distancia()