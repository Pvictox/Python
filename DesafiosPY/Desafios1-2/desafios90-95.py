#Desafio 90
'''
dados = {'nome':str(input('Digite seu nome\n')), 'media':float(input('Digite sua média\n'))}
if dados['media'] >= 7.0:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'

for k,v in dados.items():
    print(f'{k} = {v}\n')
'''
#Desafio 91
'''
from random import randint
from operator import itemgetter
jogadas = {
            'Jogador 1' : randint(1,6),
            'Jogador 2' : randint(1,6),
            'Jogador 3' : randint(1,6),
            'Jogador 4' : randint(1,6)
        }
rank = {}
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(f'{rank}')
'''
#Desafio 92
'''
import datetime
dados = dict()
dados['nome'] = str(input())
anoAtual = datetime.datetime.now().year()
dados['idade'] = int(input()) - anoAtual
dados['carteira'] = int(input())
if dados['carteira'] != 0:
    dados['anoContrato'] = int(input())
    dados['salario'] = float(input())
    dados['aposento'] = abs((anoAtual - dados['anosContrato'])-35)+idade
'''
###So mostrar
# Desafio 93
'''
soma = 0
lista = []
jogador = dict()
jogador['nome'] = str(input())
jogador['partidas'] = int(input())
for x in range(0,jogador['partidas']): 
    y = int(input())
    soma+=y
    lista.append(y)
jogador['gols'] = lista[:]
lista.clear()
jogador['total'] = soma
print(f'{jogador}')
'''
#Desafio 94
'''
pessoas = dict()
cont = 0
media = 0
mulheres = []
m = []
while True:
    l = []
    nome = str(input('nome'))
    idade = int(input())
    media += idade
    sexo = str(input())
    texto = nome + ', '+sexo
    if 'Ff' in sexo:
        mulheres.append(texto)
    l.append(texto)
    l.append(idade)
    pessoas[cont] = l[:]
    l.clear() 
    cont+=1
    char = str(input('s/n'))
    if char == 'n':
        break
media = media/(cont+1)
for x in pessoas.items()
    if x[1] > media:
        m.append(x)
'''
#Desafio 95
'''
from os import system
from operator import itemgetter
pessoa = dict()
jogadores = dict()
gols = []
lista = []
soma = 0
char = ''
cont = 0
while True:
    system('cls')
    pessoa['nome'] = str(input('nome\n'))
    pessoa['partidas'] = int(input('Partidas\n'))
    print('Digite a quantidade de gols por partida')
    for x in range(0,pessoa['partidas']):
        y = int(input())
        soma+=y
        gols.append(y)
    pessoa['gols'] = gols[:]
    gols.clear() 
    pessoa['total'] = soma
    soma = 0
    #jogadores[cont] = pessoa.copy()
    lista.append(pessoa.copy())
    pessoa.clear()
    cont+=1
    char = str(input('s/n'))
    if char == 'n':
        break
rank = sorted(lista, key=itemgetter('total'), reverse=True)
print('-='*30)
for i in rank:
    print(f'{i["nome"]}  ==  [{i["total"]}]')
'''

    
