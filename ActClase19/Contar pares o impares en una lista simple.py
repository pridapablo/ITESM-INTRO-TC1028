def main():
  n = -1
  contador_impares = 0
  contador_pares = 0
  lista = []
  valor = 0

  while valor != "*":
    lista.append(int(valor))
    valor=input()
    
  for i in range(1,n):
    lista[i] = int(input("Elemento "+str(i+1)+": "))

  for i in range(1,len(lista)):
    if lista[i] % 2 != 0:
      contador_impares = contador_impares+1
    else:
      contador_pares = contador_pares+1

  print("PARES="+str(contador_pares))
  print("IMPARES="+str(contador_impares))

if __name__ == "__main__":
  main()