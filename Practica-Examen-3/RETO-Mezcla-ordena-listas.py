def main():
  L1=[]
  L2=[]
  lista=[]

  while "*" not in L1:
    L1.append(input())

  while "*" not in L2:
    L2.append(input())

  del L1[len(L1)-1]
  del L2[len(L2)-1]

  for i in range(len(L1)):
    lista.append(L1[i])
  for i in range(len(L2)):
    lista.append(L2[i])

  lista.sort()

  print("L1=")
  print(L1)
  print("L2=")
  print(L2)
  print("LORDENADA=")
  print(lista)

if __name__ == "__main__":
  main()