def precio_antes_descuento(tipo_de_silla, cantidad) :

       if tipo_de_silla == "B" :

           precio = 700.0 * cantidad

       elif tipo_de_silla == "E" :

           precio = 900.0 * cantidad

       else :

           precio = 1500.0 * cantidad

       return precio

 

def calcula_descuento(precio, tipo_de_cl) :

       if tipo_de_cl == "F" :

           desc = precio * 0.2

       else :

           if precio >= 10000 and precio < 20000 :

               desc = precio * 0.1

           elif precio >= 20000 :

               desc = precio * 0.15

           else :

               desc = 0.0

       return desc

 

def main() :

       # pido el tipo de silla (B E L)

       tipo_silla = input("Tipo silla: ")

       # pido el tipo de cliente (N F)

       tipo_cl = input("Tipo cliente: ")

       cantidad = int(input("Cantidad de sillas: "))

       #Calculamos el precio sin descuento (precio_antes_descuento), el descuento correspondiente (calcula_descuento), el total a pagar (subtotal - desc)

       subtotal = precio_antes_descuento(tipo_silla, cantidad)

       desc = calcula_descuento(subtotal, tipo_cl)

       total = subtotal - desc

       #Imprimimos el precio antes del descuento, el descuento que corresponde y el total que el usuario va a pagar.

       #Una opcion para dar formato a lo que imprimimos y añadir variables que existen dentro de nuestro bloque de código es el uso de  f-strings. 

       # Nota que hay una f antes de las cadenas de caracteres a imprimir, y que las variables a incluir adentro de las cadenas estan rodeadas por {}.

       print(f"Total sin dcto.  ${subtotal}")

       print(f"Descuento        ${desc}")

       print(f"Total a pagar    ${total}")

 

 

if __name__=='__main__':

       main()