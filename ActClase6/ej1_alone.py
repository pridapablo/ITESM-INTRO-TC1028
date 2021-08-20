import math

radio = float(input("Ingresa el radio de la esfera: "))

def área():
    area = 4*math.pi*radio**2
    print(area)

def volumen():
    volumen = (4*math.pi*radio**3)/3
    print(volumen)

if __name__ == "__main__":
    área()
    volumen()