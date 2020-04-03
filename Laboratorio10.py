# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:30:11 2020

@author: Omar
"""
#La función realiza la potencia de b de un numero a 
def a_power_b(a,b):
#La ptencia de 0 a la 0 no está definida, para la cual se utiliza el condicinal a==0 and b==0
    if a==0 and b==0 :
        print("La potencia no está definida")
#En caso de que b sea negativo la potencia sería 1/a**b, por tanto se utiliza el condicional b<0 para identificar si b es negativo. La variable c representa la potencia normal y la variable d el resultado final
    elif b<0 :
        c = 1
        b = b*-1
        for i in range(1, b+1):
            c = (c)*a
        d = 1/c
        print(d)
#Si no se cumple ninguna de las condiciones ya planteadas, simplemente se realiza la ptencia de a**b. Utilizando una variable c para el calculo de la potencia y usando un ciclo for para multiclar a un numero de b veces
    else: 
        c = 1
        for i in range(1, b+1):
            c = (c)*a
        print(c)


#----------------------------------Principal----------------------------------#

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

a_power_b(a,b)
    
