from pygame import mixer, image,display #Importando bibliotecas 
import time
#Audio
mixer.init() #Inicialização do mixer
mixer.music.load('teste.mp3') #Carregar música
mixer.music.play() #Tocar música

#Carregando imagem
img = image.load('image.jpg') #Carrega imagem
tela = display.set_mode((536,540)) #Cria um display contendo as dimensões da imagem carregada
tela.blit(img,(0,0)) #função responsável pelo 'desenho' da imagem no canvas
display.update() #Atualização do canvas
time.sleep(2) #Espera de 2 segundos para fechar o canvas
