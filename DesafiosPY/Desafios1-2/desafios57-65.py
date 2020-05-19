#Desafio 57
'''
sexo = str(input('Digite\n')).upper()
if  sexo != 'M' and sexo != 'F':
    while not 'M' in sexo and not 'F' in sexo:
        sexo = str(input('Digite direito\n')).upper() 
'''
#Desafio 58
'''
from random import seed, randint
seed()
escolhaPC = randint(0,10)
es = int(input())
tent = 0
while es != escolhaPC:
    es = int(input()) 
    tent +=1
print(f'tentativas: {tent}')    
'''
#Desafio 59
'''
a,b = int(input()),int(input())
es = 0
print('1-Soma\n2-Multi\n3-Maior\n4-Novos\n5-Sair');
es = int(input())
while es !=5:
    if es == 1:
        print(f'{a+b}')
        es = int(input())
    elif es == 2:
        print(f'{a*b}')
        es = int(input())
    elif es==3:
        if a>b:
            print(f'{a}')
            es = int(input())
        else:
            print(f'{b}')
            es = int(input())
    else:
        a,b = int(input()),int(input())
        es = int(input())    
'''
#Desafio 60
'''
x = int(input())
fat = 1
while x >1:
    fat += fat*(x-1)
    x = x-1
print(f'{fat}')
'''
#Desafio 61/62
'''
x, r,q = int(input()),int(input()), int(input())
cont = 1
if q !=0:
    print(f'{x}', end=' ')
    while cont<q:
        print(f'{x+r}',end=' ')
        x = x+r
        cont += 1
'''
#Desafio 63
'''
n = int(input())
cont = 1
if n!=0:
    fib1,fib2,soma = 1,1,0
    print(f'{soma} {fib1} {fib2}',end=" ")
    while cont < n:
        soma = fib1+fib2
        fib1 = fib2
        fib2 = soma
        print(f'{fib2}', end=" ")
        cont +=1
'''
#Desafio 64
'''
n = 0
cont,soma=0,0
while n!= 999:
    n = int(input())
    cont +=1
    soma +=n
print(f'Cont {cont-1} Soma {soma}')
'''
#Desafio 65
'''
cond = 'b'
cont,soma = 0,0
while not 'n' in cond:
    val = int(input('Digite valor'))
    cont+=1
    soma += val
    cond= str(input('Continuar')).lower()
print(f'Media {soma/cont}')
'''

        

