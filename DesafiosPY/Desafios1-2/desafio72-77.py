#Desafio 72
'''
from time import sleep
tupla = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','cartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
rep = True
while rep:
    num = int(input())
    if num < 1 or num > 20:
        print('Digite um valor válido')
    else:
        rep = False
print(f'{tupla[num-1]}')
'''
#Desafio 73
'''
times = ('Palmeiras','Flamengo','Internacional','Gremio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
print('5 primeiros:',end=' ')
for t in range(0,5):
    print(f'{times[t]}',end=', ')
print('\n4 últimos:', end=' ')
for t in range(len(times)-4, len(times)):
    print(f'{times[t]}',end=' ')    
print('\nOrdem Alfabética:', end=' ')
print(f'{sorted(times)}', end=' ')
print(f'\nPosição da Chapecoense: {times.index("Chapecoense")}')
'''
#Desafio 74
'''
from random import randint
tupla = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
maiorRef = tupla[0]
menorRef = tupla[0]
for x in tupla:
    if x > maiorRef:
        maiorRef = x
    elif x<menorRef:
        menorRef = x
print(tupla)
print(f'Menor: {menorRef}\nMaior: {maiorRef}\n')
'''
#Desafio 75
'''
tupla = (int(input('Primeiro Valor\n')), int(input('Segundo Valor\n')), int(input('Terceiro Valor\n')),int(input('Quarto Valor\n')))
print(f'Número 9 apareceu {tupla.count(9)} vezes\n')
first =  0
pares = ''
for x in tupla:
    if x == 3:
        first = tupla.index(x)
        break
for x in tupla:
    if x%2 == 0:
        pares+=str(x)
        pares+= ' '
print(f'O número 3 apareceu pela primeira vez no índice {first}\n')
print(f'Pares: {pares}')
'''
#Desafio 76
'''
tupla = ('Carne', 10.50,'Peito de Frango', 15)
for x in range(0,len(tupla)-1,2):
    prod = tupla[x]
    preco = tupla[x+1]
    print(f'{prod}..........{preco}\n')
'''
#Desafio 77
tupla = ('casa','barro','leigo')
for x in tupla:
    print(f'A palavra {x} tem',end=' ')
    x = x.lower()
    if 'a' in x:
        print('a vogal A',end=' ')
    if 'e' in x:
        print('a vogal E',end=' ')
    if 'i' in x:
        print('a vogal I',end=' ')
    if 'o' in x:
        print('a vogal O',end=' ')
    if 'u' in x:
        print('a vogal U',end=' ')    
    print('\n')    

