# Piedra Papel o Tijeras:
def main():
       # Escribe tu código abajo de esta línea
       ana = input("Tirada de Ana: ")
       juan = input("Tirada de Juan: ")

       if len(ana) == 1 and len(juan) == 1:
           if ana in "apt" and juan in "apt":
               if ana == juan:
                   print("Empate")

               elif ana == 'a':
                   if juan == 't':
                       print("Gana Ana")
                   else:
                       print("Gana Juan")

               elif ana == 'p':
                   if juan == 'a':
                       print("Gana Ana")
                   else:
                       print("Gana Juan")

               else:
                   if juan == 'p':
                       print("Gana Ana")
                   else:
                       print("Gana Juan")

           else:
               print("Tirada incorrecta")

       else:
           print("Las tiradas deben ser un caracter")

 

if __name__ == '__main__':
       main()
