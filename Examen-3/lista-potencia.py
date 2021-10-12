def main():
    
    print("Realizado por:")
    print("Andres Fonseca Portilla")
    print("Pablo Banzo Prida")
    print("------------------------------")

    num=int(input('Ingrese el total de números que va a capturar: '))

    numeros=[]
    lista_ex=[]

    if num<=0:
        print(numeros)
        print(lista_ex)

    else:

        for i in range (num):
            numeros.append(int(input()))
        
        ex=int(input('Ingrese la potencia a la que los va a elevar: '))
        
        for i in range(len(numeros)):
            lista_ex.append(numeros[i]**ex)

        print(numeros)
        print(lista_ex)
        
if __name__=='__main__':
    main()