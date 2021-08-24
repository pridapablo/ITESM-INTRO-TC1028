import math as m

def escalera():

    altura = float(input())
    ángulo = float(input())

    largo = altura/m.sin(ángulo)

    print(round(largo))

if __name__ == "__main__":
    escalera()