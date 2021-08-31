def pies_cm(pies = 0):
    cm = 30.48*pies
    return cm #local

def pulgadas_cm(pulgadas = 0):
    cm = 2.54*pulgadas
    return cm

def yardas_cm(yardas = 0):
    cm = 91.44*yardas
    return cm


def main():
  print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
  opc = int(input("Introduce una opcion: "))
  cant = int(input("Introduce la cantidad: "))

  if opc == 1 or opc == 2 or opc == 3:
      if opc == 1:
          centimetros = pies_cm(cant) #global
          return centimetros

      elif opc == 2:
        centimetros = pulgadas_cm(cant)
        return centimetros

      elif opc == 3:
        centimetros = yardas_cm(cant)
        return centimetros
  else:
      return "Error"

if __name__ == '__main__':
    print(main())
