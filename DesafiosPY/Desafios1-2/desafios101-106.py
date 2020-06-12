#Desafio 101
'''
import datetime
def voto(ano):
    """
     -> Funcao que calcula a idade e retorna status de voto.
     :Parametro 1: ano de nascimento
    """
    anoAtual = datetime.datetime.now().year
    idade = anoAtual-ano
    if idade >=18:
        return 'Obrigatório'
    elif idade>=16 and idade<18:
        return 'Opcional'
    else:
        return 'Negado'

status = voto(2002)
print(f'{status}\n')
help(voto)
'''
#Desafio 102
'''
def fatorial(num, show = False):
    """
        -> Funcao que calcula o fatorial de um numero.
        :Parametro 1: Numero que sera calculado o fatorial.
        :Parametro 2: Valor logico que determina se o processo de calculo sera mostrado. 
    """
    total = 1
    while num > 0:
        if show == True and num>1:
            print(f'{num} * ',end=' ')
        elif show == True:
            print('1 = ', end=' ')
        total = total*num
        num = num-1
    return total

print(f'{fatorial(5)}')
'''
#Desafio 103
'''
def ficha(nome='', gols=0):
    """
        -> Funcao que monta a ficha de um jogador.
        :Param 1: Nome do jogador.
        :Param 2: Quantidade de gols.
    """
    print(f'{nome} .......... {gols}')

ficha('Carlos')
ficha('Pedro', 5)
'''
#Desafio 104
'''
def leiaInt(num):
    if type(num) != int:
        return 'Valor não inteiro'
    else:
        return num

x = leiaInt(4)
print(f'{x}')
'''
#Desafio 105
'''
def notas(*notas, show = False):
    """
     -> Função que cria um boletim com as notas fornecidas.
      :Param 1: Pacote de notas fornecidas.
      :Param 2: Opcional. Mostra a situacao da turma.
    """
    boletim = dict()
    boletim['Quantidade'] = len(notas)
    maiorRef = notas[0]
    menorRef = notas[0]
    for x in notas:
        if x > maiorRef:
            maiorRef = x
    boletim['Maior'] = maiorRef
    for x in notas:
        if x < menorRef:
            menorRef = x
    boletim['Menor'] = menorRef
    boletim['Media'] = sum(notas)/boletim['Quantidade']
    if show == True:
        if boletim['Media'] >= 7:
            boletim['Situacao'] = 'Aprovado'
        else:
            boletim['Situação'] = 'Reprovado'
    return boletim.copy()

n = notas(5.5,9.5,10,6.5, show=True)
for x,v  in n.items():
    print(f'{x} = {v}')
help(notas)
'''
#Desafios 106
print('Digite o comando.')
comando = str(input())
comando = comando.lower()
comando = comando.strip('')
help(comando)



