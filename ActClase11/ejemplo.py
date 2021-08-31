def uno (a, b) :
     a = a + 5
     b += 10
     print(a, b)
     return b
     #cuando llamemos a la función 1, en la linea 10 vamos a obtener "b"... este valor se está guardando en z (linea 11)

def main() :
     x = 5
     y = 8
     z = uno(x, y)
     print(x, y, z)

main()

##main()
#  uno(5, 8):
#    a = 5 + 5
#    b = 8 + 10
#    print(10, 18)
#    return 18

## def main() :
#    x = 5
#    y = 8
#    z = uno(x, y)
#    print(5, 8, 18)