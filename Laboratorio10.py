# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:30:11 2020

@author: Omar
"""

import numpy as np


#La función realiza la potencia de b de un numero a 

def a_power_b(a,b):
    contP = 0
    ContPar = 0
    ContImp = 0
 
        
#En caso de que b sea negativo la potencia sería 1/a**b, por tanto se utiliza el condicional b<0 para identificar si b es negativo. La variable c representa la potencia normal y la variable d el resultado final
        
    if b<0 :
            c = 1
            b = b*-1
            for i in range(1, b+1):
                c = (c)*a
            c = 1/c
            
#Si no se cumple ninguna de las condiciones ya planteadas, simplemente se realiza la ptencia de a**b. Utilizando una variable c para el calculo de la potencia y usando un ciclo for para multiclar a un numero de b veces
        
    else: 
            c = 1
            for i in range(1, b+1):
                c = (c)*a
    contP += 1
        
    if c%2==0 :
            ContPar += 1
    else:
            ContImp += 1
        
    print("El resultado de " + str(a) + " elevado a la " + str(b) + " es: " + str(c))
        
        
    print("Se calculron " + str(contP) + " potencias, " + str(ContPar) + " fueron pares " + " y " + str(ContImp) + " fueron impares")
    

def mean_arreglo(p) :
	s = 0
	for i in range(0,n):
		s += p[i]
	prom = s/n
	return prom





    
    

#----------------------------------Principal----------------------------------#

n = int(input("Ingrese el numero de parejas, mínimo 5: "))

while n<5 :
    n = int(input("Ingrese el numero de parejas, mínimo 5: "))

a = np.zeros([n])
b = np.zeros([n])
for i in range(0,n):
	a[i]=int(input("ingrese a: "))
	b[i]=int(input("ingrese b: "))

