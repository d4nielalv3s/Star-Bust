import pygame

LARGURA = 700
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
TELA_ESQUERDA = pygame.Rect(0, 0, LARGURA // 2, ALTURA)
TELA_DIREITA = pygame.Rect(LARGURA // 2, 0, LARGURA // 2, ALTURA)

def manter_dentro_dos_limites(objeto):
    if objeto.rect.left < 0:
        objeto.rect.left = 0
    if objeto.rect.right > LARGURA:
        objeto.rect.right = LARGURA
    if objeto.rect.top < 0:
        objeto.rect.top = 0
    if objeto.rect.bottom > ALTURA:
        objeto.rect.bottom = ALTURA