def main():
  n = int(input("¿Cuántos números va a ingresar? "))
  lista=[]
  for i in range(n):
    lista.append(int(input()))

  for i in range(len(lista)):
    if lista[i] % 2 == 0:
      print("pos "+str(i)+", valor "+str(lista[i]))

if __name__ == "__main__":
  main()
