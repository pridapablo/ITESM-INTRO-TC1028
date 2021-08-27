
def mayor3(n1,n2,n3):
    if n1>n2 and n1>n3:
       mayor = n1
    elif n2>n1 and n2>n3:
        mayor = n2
    elif n3>n1 and n3>n2:
        mayor = n3
    elif n1<n2 and n1<n3:
        menor = n1
    elif n2<n1 and n2<n3:
        mayor = n2
    elif n3>n1 and n3>n2:
        mayor = n3
    else:
        print ("los tres numeros son iguales")
    