'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B. 
'''
from math import pow
a,b,c = float(input()),float(input()),float(input())
print(f'TRIANGULO: {(a*c)/2:.3f}\nCIRCULO: {3.14159*pow(c,2):.3f}\nTRAPEZIO: {((a+b)*c)/2:.3f}\nQUADRADO: {pow(b,2):.3f}\nRETANGULO: {b*a:.3f}\n')