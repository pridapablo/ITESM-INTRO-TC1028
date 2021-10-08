def main():
  n = -1

  while n <= 0:
    n = int(input("¿Cuántos números deseas ingresar? (Número mayor a cero): "))

  lista = [None]*n

  for i in range(n):
    lista[i] = int(input("Elemento "+str(i+1)+": "))

  for i in range(len(lista)):
    print("lista["+str(-(i+1))+"]="+str(lista[-(i+1)]))

  lista.sort()

  print("Valor mayor:",lista[n-1])

  print("Valor menor:",lista[0])

  print(lista)

if __name__ == "__main__":
  main()