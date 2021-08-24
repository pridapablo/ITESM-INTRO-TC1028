import math as m

def phi():
    no_para_multiplicar = float(input("Número: "))
    decimales = int(input("Decimales a mostrar: "))
    
    varphi = (1 + m.sqrt(5))/2

    resultado = varphi*no_para_multiplicar

    print("Razón áurea: "+str(round(resultado,decimales)))

if __name__ == "__main__":
    phi()