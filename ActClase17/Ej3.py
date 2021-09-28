def main():
    n = int(input("Dame un número: "))
    fact = 1

    for i in range (1,n+1):
        fact = (fact * i)
    print(fact)
        
if __name__ == "__main__":
    main()