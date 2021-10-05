def main():
    
    x = 1
    y = 0

    num = int(input("Cuántos números quieres? "))

    cont = 1
    
    print(x)

    while cont < num:
        sum = x + y
        y = x
        x = sum
        print(x)

        cont += 1
        
if __name__ == "__main__":
    main()