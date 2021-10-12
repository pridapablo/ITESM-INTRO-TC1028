def cm_cm(cm):
    cm = cm % 100
    if cm != 0:
        print(str(cm) + " cm")

def cm_m(cm):
    m = cm % 100000 // 100
    if m != 0:
        print(str(m) + " m")

def cm_km(cm):
    km = cm // 100000
    if km != 0:
        print(str(km) + " km")


def main():
    cant = int(input("Introduce los cm: "))
    
    if cant == 0:
        print("Distancia igual a cero")

    elif cant == 100000:
        print("1 km")

    if cant >= 0:

        if cant < 100:
            cm_cm(cant)

        elif (cant < 100000):
            cm_m(cant)
            cm_cm(cant)

        elif cant > 100000:
            cm_km(cant)
            cm_m(cant)
            cm_cm(cant)

    else:
        print("Distancia menor a cero")

if __name__ == '__main__':
    main()
