import math

def esfera():
    radio = float(input("Ingresa el radio de la esfera: "))
    
    area = 4*math.pi*radio**2    
    volumen = (4*math.pi*radio**3)/3
    
    print("el area es ",area)
    print("el volumen es", volumen)

if __name__ == "__main__":
    esfera()