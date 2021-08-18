def main():
    #escribe tu código abajo de esta línea
    
    #El mensaje para recibir el dato debe ser **"Area a pintar en metros: ** y **Rendimiento (m2/l): ** "
    area = float(input("Area a pintar en metros: "))
    rendimiento = float(input("Rendimiento (m2/l): "))
    
    #calculo
    litros = area/rendimiento
    
    #El mensaje para la salida debe ser **"Litros a comprar: **"
    print("Litros a comprar: ",round(litros))

if __name__ == '__main__':
    main()