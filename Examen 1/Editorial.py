def costo():
    no_de_pag = int(input("Dame el número de paginas: "))
    
    resultado = (no_de_pag*60)*0.90

    print("El costo de la publicación es:",resultado)

if __name__ == "__main__":
    costo()