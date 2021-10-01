def main():
    inicial = float(input("Inserte la cantidad de dinero inicial: "))
    porcentaje = int(input("Inserte el porcentaje: "))

    intereses(inicial,porcentaje)

def intereses(c,p):
    if c > 0 and p > 0:
        p_mensual_y_decimal = p/12/100

        for i in range(12):
            c = (1+p_mensual_y_decimal) * c

        print("$"+str(c))

    else:
        print("Error en los datos")

if __name__ == "__main__":
    main()