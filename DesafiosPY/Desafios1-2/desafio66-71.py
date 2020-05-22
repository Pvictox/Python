#Desafio 66
'''
cont = soma = 0
while True:
    valor = int(input())
    if valor == 999:
        break
    cont+=1
    soma+=valor
print(f'Quantidade: {cont}\nSoma: {soma}') 
'''
#Desafio 67
'''
while True:
    val = int(input('Digite um valor\n'))
    if val<0:
        break
    for x in range(0,11):
        print(f'{val} * {x} = {val*x}\n')
'''
#Desafio 68
'''
from random import seed, randint
seed()
vit = 0
while True:
    escolhaUser = str(input('Par ou impar\n')).upper()
    val = int(input('Valor\n'))
    pcVal = randint(0,10)
    if 'IMPAR' in escolhaUser:
        escolhaPC = 'PAR'
    else:
        escolhaPC = 'IMPAR'
    num = val+pcVal
    if num%2!=0:
        if escolhaUser == 'IMPAR':
            print(f'Acertou! O numero foi {num}\n')
            vit +=1
        else:
            print(f'Errou! O numero foi {num}\nVoce ganhou {vit} vezes\n')
            break
    else:
        if escolhaUser == 'PAR':
            print(f'Acertou! O numero foi {num}\n')
            vit +=1
        else:
            print(f'Errou! O numero foi {num}\nVoce ganhou {vit} vezes\n')
            break
'''
#Desafio 69
'''
maior = quantH = quantM = 0
while True:
    idade = int(input('Digite sua Idade\n'))
    sexo = str(input('F/M?\n')).upper()
    if sexo == 'M':
        quantH +=1
    if idade > 18:
        maior+=1
        if idade<20 and sexo == 'F':
            quantM+=1
    if idade<18 and sexo == 'F':
        quantM +=1
    cont = str(input()).upper()
    if cont == 'N':
        break
print(f'{maior} {quantH} {quantM}')
'''
#Desafio 70
'''
menor,total,quant = 0
nm = ''
while true: 
    nome = str(input())
    pre = float(input)
    if menor = 0:
        menor = pre
        nm = nome
    else:
        if pre < menor:
            menor = pre
            nm = nome
    if pre >=1000:
    quant+=1
    total +=pre
    cont = str(input()).upper()
    if cont == 'N':
        break
#####So printar
'''
#Desafio 71
'''
valSacar = int(input())
ced50=ced20=ced10=ced1= 0
if valor>0:
    while True:
        if valSacar>=50:
            ced50 = valSacar//50
            valSacar = valSacar-(ced50*50)
            if valSacar == 0:
                break
        elif valSacar >=20:
            ced20 = valSacar//20
            valSacar = valSacar-(ced20*20)
            if valSacar==0:
                break
        elif valSacar>=10:
            ced10 = valSacar//10
            valSacar = valSacar-(ced10*10)
            if valSacar==0:
                break
        elif valSacar>=1:
            ced1 = valSacar
            valSacar = valSacar-ced1
            if valSacar==0:
                break
    print(f'50:{ced50}\n20:{ced20}\n10:{ced10}\n1:{ced1}')
'''


    
