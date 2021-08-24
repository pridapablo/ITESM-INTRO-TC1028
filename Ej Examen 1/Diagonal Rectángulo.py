import math as m

def diagonal():
    ancho = float(input())
    largo = float(input())

    diag = m.sqrt((ancho**2)+(largo**2))

    print(diag)

if __name__ == "__main__":
    diagonal()