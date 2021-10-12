import math as m

def crec():
    pi = int(input())
    tiempo = int(input())
    tasa = float(input())

    res = pi*(m.e**(tasa*tiempo))

    print(m.trunc(res))

if __name__ == "__main__":
    crec()