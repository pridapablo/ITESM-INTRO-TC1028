def main():
    f = float(input("Temperatura (F): "))
    c = (f-32)*(5/9)
    print("Conversión a grados Celsius: ",c,"ºC")

if __name__ == '__main__':
    main()