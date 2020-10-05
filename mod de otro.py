#Programe un método en python, en el que se le soliciten dos números enteros al usuario y el
#sistema imprima si el primero es un múltiplo del segundo.
 
def Ejercicio3():
    num = int(input("Digite un numero: "))
    num2 = int(input("Digite otro nunero: "))
 
    if num % num2 == 0:
 
        print(num, "Es multiplo de: ", num2)
    else:
        print(num, "No es multiplo de: ", num2)
 
 
Ejercicio3()
