def main():
  n_L1 = int(input())
  n_L2 = int(input())

  if (n_L1 <= 0) or (n_L2 <= 0):
    print("Error")
    exit()
  else:
    print("-----")
    L1 = []
    for i in range(n_L1):
      L1.append(input())

    print("-----")
    L2 = []
    for i in range(n_L2):
      L2.append(input())      

  print("-----")

  print(L1)
  print(L2)

  combo = []

  long1=len(L1)
  long2=len(L2)
  
  if long1<long2:
    rang_inv= -1 * ((long2+1)-(long1+1))

    for i in range(long1):
      combo.append(L1[i])
      combo.append(L2[i])

    for i in range(rang_inv,0):
      combo.append(L2[i])
    
  elif long2<long1:
    rang_inv= -1 *((long1+1)-(long2+1))

    for i in range(long2):
      combo.append(L1[i])
      combo.append(L2[i])

    for i in range(rang_inv,0):
      combo.append(L1[i])

  else:
    for i in range(long2):
      combo.append(L1[i])
      combo.append(L2[i])
      
  print(combo)

if __name__ == "__main__":
  main()