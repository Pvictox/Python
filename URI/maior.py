'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado. 
'''
a,b,c = int(input()),int(input()),int(input())
a = (a+b+abs(a-b))/2
b = (a+c+abs(a-c))/2
print(f'{b} eh o maior\n')