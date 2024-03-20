import pygame
from pygame.locals import *
from sys import exit
from personagens.taylor import Taylor_fighter
from personagens.kanye import Kanye_fighter
from utilities.bars import Barra_de_vida
from utilities.grammy import Grammy
from utilities.vma import Vma
from utilities.jordan import Jordan


pygame.init()

# dimensões cenário
largura = 1000
altura = 600

# janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Swift of Fightwest")

# framerate do jogo
relogio = pygame.time.Clock()
FPS = 45

# acrescentando o background
fundo = pygame.image.load('assets\images/background/cenario2.jpeg')

# Função para desenhar o background
# Essa parte do código é essencial para ser chamada no loop, pois sem ela os personagens não se movimentam, a imagem deles é desenhada


def bg():
    escala = pygame.transform.scale(fundo, (largura, altura))
    tela.blit(escala, (0, 0))


# Criando os personagens
Taylor_Swift = Taylor_fighter(1, 200, 310)
Kanye_West = Kanye_fighter(2, 700, 310)


# criando as barras de vida e as barras de especial dos personagens
Taylor_Swift_Bars = Barra_de_vida(1, tela)
Kanye_West_Bars = Barra_de_vida(2, tela)

#ajudar na colisao


    # só feito com o jordan
localizacao_kanye_x, localizacao_kanye_y = 0, 0
localizacao_taylor_x, localizacao_taylor_y = 0, 0

# loop
while True:
    relogio.tick(FPS)
    bg()
    Taylor_Swift_Bars.objetos(Taylor_Swift.rect, Kanye_West.rect, Taylor_Swift_Bars, Kanye_West_Bars)
    Kanye_West_Bars.objetos(Taylor_Swift.rect, Kanye_West.rect, Taylor_Swift_Bars, Kanye_West_Bars)
    # Interação de Combate
    Taylor_Swift.combate(tela, localizacao_kanye_x, localizacao_kanye_y, Kanye_West_Bars)
    Kanye_West.combate(tela, localizacao_taylor_x, localizacao_taylor_y, Taylor_Swift_Bars)
    # Movimento dos personagens
    localizacao_taylor_x, localizacao_taylor_y = Taylor_Swift.return_x_y()
    localizacao_kanye_x, localizacao_kanye_y = Kanye_West.return_x_y() # o problema deve estar aqui
    Taylor_Swift.move(largura, altura) 
    Kanye_West.move(largura, altura)
    # Desenhar os personagens
    Taylor_Swift.draw(tela)
    Kanye_West.draw(tela)
    # Desenhar as barras de vida
    Taylor_Swift_Bars.draw()
    Kanye_West_Bars.draw()
    #desenhando os objetos
  #É A QUE DETECTA COLISAO E O MOVIMENTO NO EIXO Y

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()  # ESTUDAR MUDAR PARA O FLIP 