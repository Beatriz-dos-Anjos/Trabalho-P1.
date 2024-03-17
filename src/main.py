import pygame
from pygame.locals import *
from sys import exit
from personagens.taylor import Taylor_fighter
from personagens.kanye import Kanye_fighter
from utilities.bars import Barra_de_vida
from utilities.telainicial import *


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
fundo = pygame.image.load('assets/images/background/cenario2.jpeg')

#variaveis seleçao perso
var_selecao = pygame.image.load('assets/images/background/selecao/antes_de_escolher.png').convert()

fonte = pygame.font.Font(None, 36)
branco = (255, 255, 255)

personagem_1 = fonte.render("Pressione 1 para selecionar", True, branco)
personagem_2 = fonte.render("Pressione 2 para selecionar", True, branco)


# Função para desenhar o background
# Essa parte do código é essencial para ser chamada no loop, pois sem ela os personagens não se movimentam, a imagem deles é desenhada

def bg():
    escala = pygame.transform.scale(fundo, (largura, altura))
    tela.blit(escala, (0, 0))


# Criando os personagens
#Taylor_Swift = Taylor_fighter(1, 200, 310)
#Kanye_West = Kanye_fighter(2, 700, 310)

#remover linha pois vai ser definido na tela de selaçao

# criando as barras de vida e as barras de especial dos personagens
#Taylor_Swift_Bars = Barra_de_vida(1, tela)
#Kanye_West_Bars = Barra_de_vida(2, tela)

#remover linha pois vai ser definido na tela de selaçao
    
#
localizacao_kanye_x, localizacao_kanye_y = 0, 0
localizacao_taylor_x, localizacao_taylor_y = 0, 0

#sprites da tela inicial
logo = Logo()
start = Start()
sprites.add(logo)
sprites.add(start)

#tupla para auxilinar na seleçao de personagem
personagems = ()


#variavel para controlar as cenas
cena = "menu"

# loop
while True:
    relogio.tick(FPS)
    if cena == "menu":
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'selecao'
        
        tela.blit(tela_inicial, (0,0))


        sprites.draw(tela)
        sprites.update()

    elif cena == "selecao":

        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if 'Kanye' not in personagems:
                        var_selecao = pygame.image.load('assets/images/background/selecao/p1_kanye.png').convert()
                        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
                        Kanye_West = Kanye_fighter(1, 700, 310)
                        Kanye_West_Bars = Barra_de_vida(1, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Kanye')
                        personagems = tuple(list_personagem)

                elif event.key == pygame.K_2:
                    if 'Taylor' not in personagems:
                        var_selecao = pygame.image.load('assets/images/background/selecao/p2_taylor.png').convert()
                        tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
                        Taylor_Swift = Taylor_fighter(2, 200, 310)
                        Taylor_Swift_Bars = Barra_de_vida(2, tela)
                        list_personagem = list(personagems)
                        list_personagem.append('Taylor')
                        personagems = tuple(list_personagem)

        if len(personagems) == 2:
            var_selecao = pygame.image.load('assets/images/background/selecao/escolhidos.png').convert()
            tela_selecao = pygame.transform.scale(var_selecao, (largura,altura))
            sprites.remove(logo)
            sprites.draw(tela_selecao)
            sprites.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = 'jogo'

                
        
                    
        tela.blit(tela_selecao, (0,0))
        if 'Kanye' not in personagems:
            tela.blit(personagem_1, [50, 500])
        if 'Taylor' not in personagems:
            tela.blit(personagem_2, [650, 500])

    elif cena == "jogo":
        bg()
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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    pygame.display.flip()  # ESTUDAR MUDAR PARA O FLIP 