def main():
    km = int(input("Kilómetros recorridos: "))
    litros = float(input("Litros de combustible consumidos: "))
    
    km_por_litro = km/litros
    
    print("Rendimiento Kilometros por litro: ",km_por_litro)

if __name__ == '__main__':
    main()