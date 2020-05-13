#Algumas funções para manipular texto
string = 'Eu sou uma String'
print(f'Tudo em maiúsculo: {string.upper()}\n')
print(f'Tudo em minúsculo: {string.lower()}\n')
existe = 'String' in string #Verifica se na frase existe aquilo procurado. String != STRING
print(f'Existe "STRING" na frase: {string.find("String")}\n') #O método .find() retorna a posição onde se inicia o objeto procurado
print(f'Existe "String" na frase: {existe}\n') 
print(f'A letra "u" aparece {string.count("u")} vezes na frase\n') #Conta aparições
print(f'A letra "u" aparece {string.count("u",11)} vezes na palavra String\n') #Conta aparições em um intervalo
string = string.replace("String", "Frase")
print(f'Modificação: {string}\n')
string = string.capitalize()
print(f'Correção: {string}\n')
string = string.strip() #Removendo espaços adjacentes se houver
#string = string.split() #Removendo espaços entre as palavras. Retorna uma lista
string = string.split("u", 2) #Remove o U duas vezes
print(f'Sem espaços ou U: {string}\n')
string = "-".join(string) #Junta a frase com -
print(f'Junção com "-": {string}')