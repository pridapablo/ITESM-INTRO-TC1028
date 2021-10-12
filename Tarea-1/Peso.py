def main():
    inicial = float(input("Dame el peso inicial: "))
    final = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    pormes = (inicial-final)/meses
    #diferencia entre numero de meses = peso a bajar por mes
    print("Lo que debes bajar por mes es: ",pormes)

if __name__ == '__main__':
    main()