# Pablo Banzo Prida - A01782031

def area(b,a):
    res = b*a
    return res

def area_total(area,prof,b,a):
    # res_1: dos extremos sin profundidad
    res_1 = area*2
    
    # res_2 + res_3 = 4 caras con profundidad
    res_2 = 2*(b*prof)
    res_3 = 2*(a*prof)

    #res = suma de las 6 caras en total
    res = res_1 + res_2 + res_3

    return res

def main():
    print("Realizado por: ")
    print("Pablo Banzo Prida - A01782031")
    print("-----------------------------")

    base = float(input("Dame la base: "))
    altura = float(input("Dame la altura: "))
    profundidad = float(input("Dame la profundidad: "))

    print("El área total del prisma es:", area_total(area(base,altura),profundidad,base,altura))

if __name__ == '__main__':
    main()