def  sillas(tipo, cliente, cantidad):

    if tipo == "B":
        res = cantidad*700
        print(res)

    elif tipo == "E":
        res = cantidad*900
        print(res)

    elif tipo == "L":
        res = cantidad*1_500
        print(res)

    if (20_000 < res >= 10_000) and cliente == "N":
        disc_res = res* 0.90
        desc = res * 0.10
        print(disc_res)
        print(desc)

    elif res >= 20_000 and cliente == "N":
        disc_res = res* 0.85
        desc = res*.15
        print(disc_res)
        print(desc)


    elif cliente == 'F':
        disc_res=res*0.80
        desc = res * 0.20
        print(disc_res)
        print(desc)

    else:
        return res

def clientes(cliente):
    if cliente == "F":
        return "F"
    elif cliente == "N":
        return "N"


def main():
    tipo_de_silla = str(input("Ingresa el tipo de silla: "))
    tipo_de_cliente = str(input("Ingresa el tipo de cliente: "))
    cantidad_a_comprar = int(input("Cantidad de sillas a comprar: "))

    sillas(tipo_de_silla,clientes(tipo_de_cliente),cantidad_a_comprar)
    
if __name__ == '__main__':
    main()