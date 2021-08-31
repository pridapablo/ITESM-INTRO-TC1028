def pies_cm(pies):
    resultado = 30.48*pies
    return resultado

def pulgadas_cm(pulgadas):
    resultado = 2.54*pulgadas
    return resultado

def yardas_cm(yardas):
    resultado = 91.44*yardas
    return resultado

def main():
  print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
  eleccion = int(input("Introduce una opcion: "))
  cantidad = int(input("Introduce la cantidad: "))

  if eleccion == 1:
      pies_cm(cantidad) 
    
  elif eleccion == 2:
      pulgadas_cm(cantidad)

  elif eleccion == 3:
      yardas_cm(cantidad)

  else:
      print("Error")

if __name__ == '__main__':
    main()