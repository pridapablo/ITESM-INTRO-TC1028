def main():

    art1 = float(input("Primer articulo: $"))
    art2 = float(input("Segundo articulo: $"))
    art3 = float(input("Tercer articulo: $"))
    
    total = art1+art2+art3
    descuento = total*.85
    
    print("Total de la compra: $",total)
    print("Total con 15% de descuento: $",descuento)

if __name__ == '__main__':
    main()