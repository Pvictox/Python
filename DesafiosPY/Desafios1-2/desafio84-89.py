#Desafio 84
'''
import os
f = True
pessoa =[]
pesadas =[]
leves = []
cont = 0
char = ''
while f:
    os.system('cls')
    pessoa.append(str(input('Digite seu nome\n')))
    pessoa.append(float(input('Digite seu peso\n')))
    cont +=1
    print(f'{pessoa[1]}')
    if pessoa[1] > 70:
        pesadas.append(pessoa[:])
    else:
        leves.append(pessoa[:])    
    pessoa.clear()
    print('Deseja continuar[S/N]')
    char = str(input()).lower()
    if char == 'n':
        f = False
print(f'{cont} pessoas foram cadastradas\nLeves: {leves[0]}\nPesadas: {pesadas}')
'''
#Desafio 85
'''
listaPar = []
listaImpar = []
numeros = []
for x in range (0,7):
    y = int(input())
    if y%2==0:
        if not y in listaPar: 
            listaPar.append(y)
    else:
        if not y in listaImpar:
            listaImpar.append(y)
listaPar.sort()
listaImpar.sort()
numeros.append(listaPar[:])
numeros.append(listaImpar[:])
listaPar.clear()
listaImpar.clear()
print(f'{numeros}')
'''
#Desafio 86 e 87
'''
numero = []
matriz = []
cont = 1
somaPar = 0
for x in range(0,9):
    numero.append(int(input()))
    if numero[0]%2==0:
        somaPar+=numero[0]
    matriz.append(numero[:])
    numero.clear()
for x in matriz:
    if cont == 3:
        print(f'{x}\n')
        cont = 1
    else:
        print(f'{x}',end=' ')
        cont = cont+1
print(f'\nSoma dos pares: {somaPar}\n')
soma3Coluna = int(matriz[2])+int(matriz[5][0])+int(matriz[8][0])
print(f'Soma 3 Coluna: {soma3Coluna}')
cont = 0
maiorRef = matriz[3]
for x in matriz:
    if cont > 3 and cont < 6:
        if matriz[cont] > maiorRef:
            maiorRef = matriz[cont]
    cont+=1
print(f'O maior da segunda coluna é {maiorRef}')
'''
#Desafio 88
'''
from random import randint, seed
seed()
jogos = int(input('Quantos jogos?\n'))
numeros = []
aposta =[]
cont = 0
for x in range(0,jogos):
    while cont < 6:
        numeros.append(randint(1,60))
        cont+=1
    aposta.append(f"Jogo {x+1} "+str(numeros[:]))
    numeros.clear()
    cont = 0
print(f'{aposta}')
'''
#Desafio 89
from os import system
f = True
alunos = []
boletim = []
nome = char = ''
nota1 = nota2 = escolha = 0
while f:
    system('cls')
    nome = str(input('Nome\n')).capitalize()
    alunos.append(nome)
    nota1 = float(input('Nota 1\n'))
    nota2 = float(input('Nota2\n'))
    alunos.append((nota1+nota2)/2)
    boletim.append(alunos[:])
    alunos.clear()
    char = str(input('Continuar\n')).lower()
    if char == 'n':
        f = False
print('1 - Todos\n2 - Individual\n')
escolha = int(input())
if escolha == 1:
    for x in boletim:
        print(f'{x[0]}.......{x[1]}\n')
else:
    nome = str(input()) .capitalize()
    for x in boletim:
        if nome == x[0]:
            print(f'{nome}....{x[1]}\n')
    