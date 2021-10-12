def main():
  n = int(input("¿Cuántos números va a ingresar? "))
  lista=[]
  valores_unicos=[]

  for i in range(n):
    lista.append(input())

  if len(lista) <= 0:
    print("Error")

  else:
    print(lista)

    for elemento in lista:
      if elemento not in valores_unicos:
        valores_unicos.append(elemento)

    print(valores_unicos)

if __name__ == "__main__":
  main()
