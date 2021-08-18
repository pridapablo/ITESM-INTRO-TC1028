def main():
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    costo = (mensajes*0.8)+(megas*0.8)+(minutos*0.8)
    print("El costo mensual es: ",costo)

if __name__ == '__main__':
    main()