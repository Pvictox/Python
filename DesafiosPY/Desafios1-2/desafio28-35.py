#Desafio 28
'''
import random
random.seed()
num = random.randint(0,5)
x = int(input())
if num == x:
    print('Voce acertou\n')
else:
    print('Voce errou')
    print(f'O número era {num}\n')
'''
#Desafio 29
'''
km = float(input())
if km > 80:
    print('Foi multado\n')
    print(f'O valor da multa é: {(km-80)*7}\n')
'''
#Desafio 30
'''
num = int(input())
print('É par' if num%2==0 else 'É impar')
'''
#Desafio 31
'''
km = float(input())
print(f'{0.50*km}\n' if km<=200 else f'{0.45*km}')
'''
#Desafio 32
'''
ano = int(input())
if ano%4==0 and ano%100!=0:
    print('Bissexto\n')
elif ano%400==0:
    print('Bissexto')
else:
    print('Nao é\n')
'''
#Desafio 33
'''
x,y,z = int(input()),int(input()),int(input())
if x>y and x>z:
    print(f'Maior {x}\n')
    if y>z:
        print(f'Menor {z}\n')
    else:
        print(f'Menor {y}\n')    
elif y>x and y>z:
    print(f'Maior {y}\n')
    if x>z: 
        print(f'Menor {z}\n')
    else:
        print(f'Menor {x}\n')
else:
    print(f'Maior {z}\n')
    if x>y:
        print(f'Menor {y}\n')
    else:
        print(f'Menor {x}\n')
'''
#Desafio 34
'''
sal = float(input())
print(f'{(10*sal)/100}\n' if sal > 1250 else f'{(15*sal)/100}')
'''
#Desafio 35
a, b, c = float(input()),float(input()),float(input())
print(f'E triangulo\n'if (abs(b-c)<a and a<b+c) and (abs(a-c)<b and b<a+c) and (abs(a-b)<c and c<b+a) else 'Não e' )