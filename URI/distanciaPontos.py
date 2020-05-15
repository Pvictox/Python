'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) 
e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
'''
x1,y1,x2,y2 = float(input()),float(input()),float(input()),float(input())
from math import pow, sqrt
print(f'{sqrt(pow((x2-x1),2)+pow((y2-y1),2)):.4f}\n')
