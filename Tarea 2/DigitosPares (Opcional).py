# nota: cero es par

def main():
    entrada = int(input("Dame un número: "))
    i = 0 # yo se que no hemos aprendido iteraciones, pero creo que es la forma más fácil de hacerlo
    count = 0 # inicializo el iterador y el conteo en cero porque si no no corre la función

    if (entrada < 9999) and (entrada > 999): # test 4 dígitos donde el primero no es cero

        entrada_cadena = str(entrada) #convierto la entrada en cadena para poder recorrer sus índices

        for i in range(0, 4): # lo hago 4 veces
            if int(entrada_cadena[i]) % 2 == 0: # si el residuo es cero...
                count = count + 1 # entonces sumo 1 a la cuenta
    
        print("El número de dígitos pares es: ", count) # imprimo la cuenta que llevo

    else:
        print("Por favor ingresa un número de 4 dígitos que no comience con cero") # mensaje de error

if __name__ == '__main__':
    main()