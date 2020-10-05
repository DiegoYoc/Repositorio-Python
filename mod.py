# -*- coding: utf-8 -*-
 
def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 
# lista que contendra los valores multiples
multiples_3=[]
multiples_5=[]
 
# bucle del 1 al 100
for i in range(1,101):
 
    if multiple(i,3):
        multiples_3.append(i)
 
    if multiple(i,5):
        multiples_5.append(i)
 
print ("Los multiples de 3 son:", multiples_3)
print ("")
print ("Los multiples de 5 son:", multiples_5)
