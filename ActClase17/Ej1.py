def main():
    n = int(input("Dame un número: "))

    for i in range(1,n):
        print(i,end=", ")
    
    print(n,end="") 

if __name__ == "__main__":
    main()