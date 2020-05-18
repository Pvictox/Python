#desafio 46
'''
from time import sleep
y = 10
for x in range(-1,10):
    print(f'{y}\n')
    y=y-1
    sleep(1)
'''
#Desafio 47
'''
for x in range(1,51):
    if x%2==0:
        print(f'{x}\n')
'''
#Desafio 48
'''
sum =0
for x in range (1,501):
    if x%2 != 0 and x%3==0:
        sum = sum+x
print(f'{sum}\n')
'''
#Desafio 49
'''
num = float(input())
for x in [0,1,2,3,4,5,6,7,8,9,10]:
    print(f'{num:.2f} * {x}= {num*x:.2f}\n')
'''
#Desafio 50
'''
sum = 0
for x in range(0,6):
    y = int(input())
    if y%2==0:
        sum = sum+y
print(f'{sum}')
'''
#Desafio 51
'''
prim, raz = int(input()),int(input())
for x in range(0,10):
    print(f'{prim}')
    prim = prim+raz
'''
#Desafio 52
'''
num = int(input())
primo = True
if num == 1 or num==2:
    primo = False
for x in range (2,num//2):
    if num%x == 0:
        primo = False
        break
if primo:
    print('Primo')
else:
    print('Não e')
'''
#Desafio 53
'''
frase = str(input())
igual = 0
frase = frase.lower()
if " " in frase:
    frase = frase.split()
    frase = "".join(frase)
for x in range(0,len(frase)):
    if frase[x] == frase[(len(frase)-1)-x]:
        igual = igual+1
if igual == len(frase):
    print('Palindromo')        
'''
#Desafio 54
'''
import datetime
anoAtual = datetime.datetime.now().year
cont = 0
cont2 = 0
for x in range(0,7):
    ano = int(input())
    idade = anoAtual - ano
    if idade >= 18:
        cont = cont+1
    else:
        cont2 = cont2+1
print(f'Maiores: {cont}\nMenores: {cont2}')
'''
#Desafio 55
'''
pesoRefMa = 0
pesoRefMe = 0 
maiorPeso, menorPeso = 0,0
for x in range(0,5):
    peso = float(input())
    if menorPeso == 0:
        menorPeso = peso
        pesoRefMe = peso
    if peso > pesoRefMa:
        maiorPeso = peso
        pesoRefMa = maiorPeso
    if peso < pesoRefMe:
        menorPeso = peso
        pesoRefMe = menorPeso
print(f'Maior {maiorPeso}\nMenor {menorPeso}')
'''
#Desafio 56
somaIdade =0
idadeHRef = 0
hMaisVelho = ''
contMulher =0
for x in range(0,4):
    nome,sexo = str(input('Nome\n')),str(input('Sexo\n'))
    idade = int(input('Idade\n'))
    somaIdade = somaIdade+idade
    if 'm' in sexo:
        if idadeHRef==0:
            idadeHRef = idade
            hMaisVelho = nome
        else:
            if idade>idadeHRef:
                idadeHRef = idade
                hMaisVelho = nome
    if 'f' in sexo:
        if idade<20:
            contMulher = contMulher+1

print(f'Media de idades: {somaIdade/4}\nHomem mais velho: {hMaisVelho}\nQuant mulher menor que 20: {contMulher}')


    