from Utils.Telas import *
from Utils.Cores import *
from sys import exit
from Jogador import Jogador
from Bola import Bola
from IA import IA
from Trave import Trave

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Star-Ball')
running = True

jogador = Jogador()
bola = Bola()
ia = IA()
trave = Trave()

relogio = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            exit()

    trave.desenhar()
    trave.bloquear(ia.rect, jogador.rect)
    jogador.movimentacao()
    ia.movimentacao_ia()
    jogador.agarrar(bola)
    jogador.colisao_arremesso(bola)
    if bola in TELA_ESQUERDA:
        ia.persequir(bola)
    if pygame.sprite.collide_rect(bola, ia):
        bola.pos_colisao(ia)

    tela.fill(COR_BRANCA)
    tela.blit(bola.image, bola.rect)
    tela.blit(ia.image, ia.rect)
    tela.blit(trave.image, trave.rect)
    tela.blit(jogador.image, jogador.rect)
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
exit()
