def main():
    #inicializo en cero para entrar a bucle
    edad = 0
    año = 0
    while (edad or año) <=0:
        #hasta que no se cumple que sean enteros positivos el programa se repite
        #-> esto lo hice porque se pide en el ejercicio (se que no era necesario)
        edad = int(input("Dame tu edad: "))
        año = int(input("Dame el año actual: "))
    
    #calculo
    cumpliras = (año - edad)+100
    
    print("Cumplirás 100 años en el año: ",cumpliras)

if __name__ == '__main__':
    main()