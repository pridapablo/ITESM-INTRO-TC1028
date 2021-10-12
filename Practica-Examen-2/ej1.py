# Escribe una función llamada equivalente que reciba como parámetro una cantidad de horas,
# minutos y segundos y regrese como valor de retorno el tiempo equivalente en segundos.

def equivalente(horas, minutos, segundos):
    res_par1 = horas * 3600
    res_par2 = minutos * 60
    
    res = res_par1 + res_par2 + segundos

    return res

def main():
    print("PROCESO 1")
    hrs_1 = int(input("Horas: "))
    min_1 = int(input("Minutos: "))
    seg_1 = int(input("Segundos: "))

    proceso_1 = equivalente(hrs_1,min_1, seg_1)
    print("El proceso 1 tomó " + str(proceso_1) + " segundos")


    print("PROCESO 2")
    hrs_2 = int(input("Horas: "))
    min_2 = int(input("Minutos: "))
    seg_2 = int(input("Segundos: "))

    proceso_2 = equivalente(hrs_2,min_2, seg_2)
    print("El proceso 2 tomó " + str(proceso_2) + " segundos")


if __name__ == "__main__":
    main()