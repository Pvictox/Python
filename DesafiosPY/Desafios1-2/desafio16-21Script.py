#Desafio 16
'''
from math import floor
n = float(input())
print(f'{floor(n)}')
'''
#Desafio 17
'''
from math import sqrt,pow
cat1, cat2 = float(input()), float(input())
hip = pow(cat1,2)+pow(cat2,2)
print(f'{sqrt(hip)}')
'''
#Desafio 18
'''
from math import sin, cos,tan
ang = int(input())
print(f'Seno: {sin(ang):.1f}\nCosseno: {cos(ang):.1f}\nTangente: {tan(ang):.1f}')
'''
#Desafio 19
'''
from random import choice,seed
seed()
n1,n2,n3,n4 = input(),input(),input(),input()
print(f'O escolhido foi {choice([n1,n2,n3,n4])}')
'''
#Desafio 20
'''
from random import sample
n1,n2,n3,n4 = input(),input(),input(),input()
print(f'{sample([n1,n2,n3,n4],4)}')
'''
#Desafio 21
from pygame import mixer
mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()

