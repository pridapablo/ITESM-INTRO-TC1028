def main():
  n = -1
  suma = 0

  while n <= 0:
    n = int(input("¿Cuántos números deseas ingresar? (Número mayor a cero): "))

  lista = [None]*n

  for i in range(n):
    lista[i] = int(input("Elemento "+str(i+1)+": "))

  for i in range(len(lista)):
    print("lista["+str(i)+"]="+str(lista[i]))

  print("Último elemento:", lista[n-1])

  for i in range(len(lista)):
    suma = suma+lista[i]

  print("Suma:", suma)

  promedio = suma/n

  print("Promedio:", promedio)

if __name__ == "__main__":
  main()