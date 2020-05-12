'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre o número e o salário do funcionário, com duas casas decimais. 
'''
number, hours = int(input()), int(input())
valPerHr = float(input())
print(f'NUMBER = {number}\nSALARY = U$ {valPerHr*hours:.2f}\n')