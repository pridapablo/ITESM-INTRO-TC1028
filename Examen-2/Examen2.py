# Pablo Banzo Prida - A01782031
# Andrés Fonseca Portilla - A01782415

def  tarjeteria(papel, plumon):
    totalpapel = (12*papel)
    capplumon = (35*plumon)

    if totalpapel > capplumon:
        return capplumon
    elif totalpapel < capplumon:
        return totalpapel
    else:
        return totalpapel or capplumon


def main():
    print("Realizado por: ")
    print("Pablo Banzo Prida - A01782031")
    print("Andrés Fonseca Portilla - A01782415")
    print("-----------------------------")

    cantpapel = int(input("Dame la cantidad de pliegos de papel albanene: "))
    cantplumon = int(input("Dame la cantidad de plumones: "))

    print("El número máximo de tarjetas que se pueden hacer es: ", tarjeteria(cantpapel,cantplumon))

if __name__ == '__main__':
    main()