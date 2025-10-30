# La calculadora de digitos 
# //// //// //// //// //// /// //// //// /// //// //// ///

Digitos = []

def sumadoraDig(numero):
    if numero < 10:
        Digitos.append(numero) 
        return numero
    else:
        ultimo = numero % 10
        Digitos.append(ultimo)
        resto = numero // 10         
        return ultimo + sumadoraDig(resto)

def main():
    print("""     _____La calculadora que calcula_____
          _______________________________________________ 
          """)
    numero = int(input("Para iniciar, digite un numero positivo entero:  "))
    if numero < 0:
        print("Error: Porfavor verifique que el numero sea positivo y entero")
    else:
        total = sumadoraDig(numero)
        Digitos.reverse()  
        print("\nLos dígitos encontrados son:", Digitos)
        print("Su suma es de: ", total)
main()