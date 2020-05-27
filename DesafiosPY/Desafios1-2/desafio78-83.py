#DESAFIO 78
'''
ista = []
for x in range(0,5):
    lista.append(int(input()))
menorRef = maiorRef = lista[0]
indMen = indMai = 0
for x in lista:
    if x<menorRef:
        menorRef = x
        indMen = lista.index(x)
    elif x>maiorRef:
        maiorRef = x
        indMai = lista.index(x)
print(f'Menor: {menorRef}\nMaior: {maiorRef}\nIndex Menor: {indMen}\nIndex Maior:{indMai}')
'''
#Desafio 79
'''
f = True
l = []
char = ''
while f:
    x = int(input())
    if not x in l:
        l.append(x)
    print('Continuar? S/N')
    char = str(input()).lower()
    if char == 'n':
        f = False
l.sort()        
print(f'{l}')
'''
#Desafio 80
'''
l = []
t = 0
for x in range(0,4):
    l.append(int(input()))

for i in range(0,4):
    for j in range(0,4):
        if l[i] < l[j]:
            t = l[i]
            l[i] = l[j]
            l[j] = t
print(f'{l}') 
'''
#Desafio 81
'''
f = True
l = []
cont = 0
char = ''
while f:
    l.append(int(input('Digite o valor\n')))
    cont +=1
    print('Continuar?')
    char = str(input()).lower()
    if char == 'n':
        f = False
l.sort(reverse=True)    
print(f'Voce digitou {cont} numeros\nInverso: {l}\n5 está na lista: {5 in l}')
'''
#Desafio 82
'''
l = []
lPar = []
lImpar = []
f = True
char = 'n'
while f:
    l.append(int(input()))
    print('Continuar?')
    char = str(input()).lower()
    if char == 'n':
        f = False
for x in l:
    if x%2==0:
        lPar.append(x)
    else:
        lImpar.append(x)
print(f'Lista {l}\nLista Par: {lPar}\nLista Impar: {lImpar}')
'''
#Desafio 83
'''
esp = str(input('Digite a expressão\n'))
contFechado = contAberto=0
for x in range(0,len(esp)):
    if esp[x] == '(':
        contAberto +=1
    elif esp[x]==')' and contAberto==0:
        contFechado = -1
        break
    if esp[x] == ')' and contAberto!=0:
        contFechado+=1

if contFechado == contAberto:
    print('Expressão OK')
else:
    print('Expressão Errada')
'''


    