def main():
  n = int(input("¿Cuántos términos de la serie de Fibonacci desea? "))

  while n < 0:
    n = int(input("Error, el dato recibido debe ser mayor que cero. ¿Cuántos términos de la serie de Fibonacci desea? "))

  if n == 0:
    lista = []
  elif n == 1:
    lista = [0]
  else:
    lista = [0,1]
    for i in range(2,n):
        lista.append(lista[i-2]+lista[i-1])

  print(lista)

if __name__ == "__main__":
  main()