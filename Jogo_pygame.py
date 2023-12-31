import pygame
from random import randint

pygame.init()
pygame.display.set_caption('Resgate Real') #nome da janela
pygame.key.get_focused() #reconhecer o teclado

tela = pygame.display.set_mode((600,600))#definindo a resolução da tela

#pegar as imagens na pasta
fundo = pygame.image.load('imagens/Grama.jpg')
fundo = pygame.transform.scale(fundo,(200,200)) #redimensionar a imagem da grama
mapa = pygame.image.load('imagens/Mapa.png')
mapa = pygame.transform.scale(mapa, (400,400))
barreira = pygame.image.load('imagens/Barreira.png')
barreira = pygame.transform.scale(barreira, (41,41))

char = pygame.image.load('imagens/Cavaleiro.png')
princ = pygame.image.load('imagens/Princesa.png')
princ = pygame.transform.scale(princ, (38,38)) #redimensionar a imagem da princesa
monstro = pygame.image.load('imagens/Monstro.png')
monstro = pygame.transform.scale(monstro, (43,43))

imvida = pygame.image.load('imagens/Heart.png')
impassos = pygame.image.load('imagens/Passos.png')
impassos = pygame.transform.scale(impassos,(40,29)) #redimensionar a imagem do tênis


#posição do personagem
charx = 100 + (40*randint(0,9))
chary = 100 + (40*randint(0,9))

#status
vida = 3
passos = 20

#escrever na tela
fonte = pygame.font.SysFont('pixelart', 40)
mensagem = fonte.render(str(passos),False,(255,255,255)) #número de passos na tela

prinx = charx
priny = chary

qntbar = 3

while charx == prinx or chary == priny:
    prinx = 100 + (40*randint(0,9)) #posição da princesa
    priny = 100 + (40*randint(0,9))

cordbarreiras = []
condicao = [chary, chary-40, chary+40, charx, charx-40, charx+40, prinx, prinx-40, prinx+40, priny, priny-40,priny+40]

for a in range(0,qntbar):
    cordbarreiras.append([])
    cordbarreiras[a].append(charx)
    cordbarreiras[a].append(chary)


while any((cordbarreiras[a][b] for a in range(0,3) for b in range(0,2)) == condicao[c] for c in range(0,12)):
    for a in range(0,qntbar):
        for b in range(0,2):
            cordbarreiras[a][b] = 100 + (40*randint(0,9))
    print(cordbarreiras)


barcolision = []
for a in range(0,qntbar):
    barcolision.append([])
    for b in range(0,2):
        barcolision[a].append(pygame.Rect(cordbarreiras[a][0]-40,cordbarreiras[a][1],120,40))
        barcolision[a].append(pygame.Rect(cordbarreiras[a][0],cordbarreiras[a][1]-40,40,120))

#para rotacionar o personagem ao trocar de lado
girou = False
#algumas variáveis para o funcionamento do jogo
rodando = True

durante = True
ganhou = False
perdeu = False


clock = pygame.time.Clock()





while rodando:
    dt = clock.tick(60)
    if durante == True:
        
        charcolision = pygame.Rect(charx,chary,40,40)
        tela.fill((0,0,0))
        for a in range(1,4):
            tela.blit(fundo,(100,100*a))#grama
            tela.blit(fundo,(300,100*a))

        for a in range(0,12):
            tela.blit(barreira,(60+40*a, 60))
            tela.blit(barreira,(60+40*a,500))
            tela.blit(barreira,(60,60+40*a))
            tela.blit(barreira,(500, 60+40*a))

        for a in range(0,qntbar):
            for b in range(-1,2):
                tela.blit(barreira,(cordbarreiras[a][0], cordbarreiras[a][1]+40*a))
                tela.blit(barreira,(cordbarreiras[a][0]+40*a, cordbarreiras[a][1]))

        
        tela.blit(mapa,(100,100)) #aqui são aqueles quadrados pretos
        tela.blit(char, (charx,chary)) #personagem
        tela.blit(princ, (prinx, priny))#princesa

        tela.blit(impassos, (55,45))#aqui é a imagem do tênis
        tela.blit(mensagem, (20,50))#aqui é o número de passos
        for a in range(0, vida):
            tela.blit(imvida, (10+30*a,10))
        
        #fechar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            #andar
           
            if event.type == pygame.KEYDOWN:
                
            
                if event.key== pygame.K_w or event.key == pygame.K_UP:
                    if (chary == 100) or any(pygame.Rect(charx, chary-40, 40,40).colliderect(barcolision[a][b]) for a in range(0,2) for b in range(0,2)):
                        pass
                    else:
                        chary -= 40
                        passos -= 1
                if event.key== pygame.K_s or event.key == pygame.K_DOWN:
                    if (chary == 460) or any(pygame.Rect(charx, chary+40, 40,40).colliderect(barcolision[a][b]) for a in range(0,2) for b in range(0,2)): 
                        pass
                    else:
                        chary += 40
                        passos -= 1
                if event.key== pygame.K_a or event.key == pygame.K_LEFT:
                    if charx == 100 or any(pygame.Rect(charx-40, chary, 40,40).colliderect(barcolision[a][b]) for a in range(0,2) for b in range(0,2)):  
                        pass
                    else:
                        if girou == False:
                            char = pygame.transform.flip(char,1,0)
                            girou = True
                        charx -= 40
                        passos -= 1
                if event.key== pygame.K_d or event.key == pygame.K_RIGHT:
                    if charx == 460 or any(pygame.Rect(charx+40, chary, 40,40).colliderect(barcolision[a][b]) for a in range(0,2) for b in range(0,2)): 
                        pass
                    else:
                        if girou == True:
                            char = pygame.transform.flip(char,1,0)
                            girou = False
                        charx += 40
                        passos -= 1
                if event.key == pygame.K_v:
                    vida -= 1
                if event.key == pygame.K_j:
                    vida += 1
                if event.key == pygame.K_l:
                    passos += 100
           

        if chary == priny and charx == prinx:
            ganhou = True
            durante = False
        if vida == 0:
            perdeu = True
            durante = False
        if passos <= 0:
            perdeu = True
            durante = False
        

        mensagem = fonte.render(str(passos),False,(255,255,255),(0,0,0))
        
    elif perdeu == True:
        tela.fill((0,0,0))
        mensagem = fonte.render('Perdeu kkkkkkk',False,(255,255,255),(0,0,0))
        tela.blit(mensagem, (200,270))   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        
    
    elif ganhou == True:
        tela.fill((0,0,0))
        mensagem = fonte.render('Você ganhou!',False, (255,255,255))
        tela.blit(mensagem, (200,270))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
               
    pygame.display.flip()

