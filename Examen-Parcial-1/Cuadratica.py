# Pablo Banzo Prida - A01782031

import math as m

def main():
    print("Realizado por: ")
    print("Pablo Banzo Prida - A01782031")
    print("-----------------------------")

    a = int(input("Da el valor de a: "))
    b = int(input("Da el valor de b: "))
    c = int(input("Da el valor de c: "))

    chicharronera = m.pow (b,2)-4*a*c

    if a==0 and b==0:
        print ("No tiene solución")
    elif a==0 and b != 0:
        x = (-(c))/b
        print(x)
    elif a != 0 and b != 0:
        disc = b**2-4*a*c
        if disc < 0:
            print("Raices complejas")
        elif disc > 0:
            x1=(-b+m.sqrt(chicharronera))/2*a
            x2=(-b-m.sqrt(chicharronera))/2*a
            print(x1)
            print(x2)
        elif disc == 0:
            x1=(-b+m.sqrt(chicharronera))/2*a
            print(x1)

if __name__ == '__main__':
    main()