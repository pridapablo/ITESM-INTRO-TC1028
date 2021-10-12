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
    lista.append(int(L1[i]))
  for i in range(len(L2)):
    lista.append(int(L2[i]))

  lista.sort()

  print("L1=")
  print("[",end="")
  if len(L1) != 0:
    for i in range(len(L1)-1):
      print(str(L1[i]),end=", ")
    print(L1[-1],end="")
  print("]")
  
  print("L2=")
  print("[",end="")
  if len(L2) != 0:
    for i in range(len(L2)-1):
      print(str(L2[i]),end=", ")
    print(L2[-1],end="")
  print("]")

  print("LORDENADA=")
  print("[",end="")
  if len(lista) != 0:
    for i in range(len(lista)-1):
      print(str(lista[i]),end=", ")
    print(lista[-1],end="")
  print("]")

if __name__ == "__main__":
  main()