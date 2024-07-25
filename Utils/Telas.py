import pygame

LARGURA = 700
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
TELA_ESQUERDA = pygame.Rect(0, 0, LARGURA // 2, ALTURA)
TELA_DIREITA = pygame.Rect(LARGURA // 2, 0, LARGURA // 2, ALTURA)
