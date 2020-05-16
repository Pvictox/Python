#Desafio 36
'''
valorCasa,salario = float(input('Valor da casa')),float(input('Salario'))
anos = int(input('Anos'))
prestacao = valorCasa/(12*anos)
if prestacao>(30*salario)/100:
    print('Prestação excedeu salario')
else:
    print('Empréstimo aprovado')
'''
#Desafio 37
'''
num = int(input())
print('1 - Binario\n2 - Octal\n3 - Hexadecimal\n')
escolha = int(input())
if escolha == 1:
    print(f'O valor de {num} em binario é: {bin(num)[2:]}')
elif escolha == 2:
     print(f'O valor de {num} em Octal é: {oct(num)[2:]}')
else:
    print(f'O valor de {num} em Hexadecimal é: {hex(num)[2:]}')
'''
#Desafio 38
'''
a,b = int(input()),int(input())
if a>b:
    print(f'{a} é maior que {b}\n')
elif a<b: print(f'{b} é mario que {a}\n')
else: 
    print('São iguais\n')
'''
#Desafio 39
'''
import datetime
ano = int(input())
agora = datetime.datetime.now()
idade = agora.year-ano
if idade>18:
    print(f'Passou do tempo. Voce está {idade-18} anos atrasado\n')
elif idade<18:
    print(f'Ainda vai se alistar. Falta {18-idade} anos\n')
else:
    print('Tá na hora de se alistar\n')    
'''
#Desafio 40
'''
n1,n2 = float(input()), float(input())
if ((n1+n2)/2) < 5.0:
    print('Reprovado\n') 
elif ((n1+n2)/2) >= 7.0:
    print(f'Aprovado\n')
else:
    print(f'Recuperação\n')
'''
#Desafio 41
'''
import datetime
ano = int(input())
idade = datetime.datetime.now()
idade = idade.year-ano
if idade <= 9:
    print(f'Mirim\n')
elif idade<=14:
    print(f'Infantil\n')
elif idade<=19:
    print(f'Junior\n')    
elif idade==20:
    print(f'Senior\n')
else:
    print(f'Master\n')
'''
#Desafio 42
'''
a, b, c = float(input()),float(input()),float(input())
if (abs(b-c)<a and a<b+c) and (abs(a-c)<b and b<a+c) and (abs(a-b)<c and c<b+a):
    if a==b==c:
        print('Equilatero')
    elif a==b or a==c or b==c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Nao e')
'''
#Desafio 43
'''
peso, altura = float(input()),float(input())
imc = peso/altura**2
if imc <18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc <=25:
    print('Peso ideal')
elif imc<=30:
    print('Sobrepeso')
elif imc <=40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
'''
#Desafio 44
'''
preco = float(input())
cond = str(input()).capitalize()
if 'A vista' in cond:
    if 'dinheiro' in cond or 'cheque' in cond:
        preco = preco-((10*preco)/100)
    elif 'cartão' in cond:
        preco = preco-((5*preco)/100)
elif '2x' in cond:
    print(f'{preco}')
elif '3x' in cond:
    preco = preco+((20*preco)/100)
print(f'{preco}')
'''
#Desafio 45
'''
from random import randint,seed
seed()
escolhas = ['Pedra','Papel','Tesoura']
escolhaPC = escolhas[randint(0,2)]
suaEscolha = str(input()).capitalize()
if suaEscolha == escolhaPC:
    print(f'Empate\n')
    print(f'O pc escolheu {escolhaPC}\n')
elif (suaEscolha == 'Papel' and escolhaPC=='Pedra') or (suaEscolha=='Pedra' and escolhaPC=='Tesoura') or (suaEscolha=='Tesoura' and escolhaPC=='Papel'):
    print(f'Voce ganhou\n')
    print(f'O pc escolheu {escolhaPC}\n')
else:
    print(f'Voce perdeu\n')
    print(f'O pc escolheu {escolhaPC}\n')
'''


    