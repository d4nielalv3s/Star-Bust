from Utils.Cores import *
from Utils.Telas import *

class Trave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((8, ALTURA))
        self.image.fill(COR_PRETA)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA

    def bloquear(self, ia_rect, jogador_rect):
        if self.rect.colliderect(ia_rect):
            if ia_rect.left < self.rect.left:
                ia_rect.left = self.rect.left + 10
            if ia_rect.left > self.rect.left:
                ia_rect.left = self.rect.left - 10
            if ia_rect.right > self.rect.right:
                ia_rect.right = self.rect.right - 10

        if self.rect.colliderect(jogador_rect):
            if jogador_rect.left < self.rect.left:
                jogador_rect.left = self.rect.left + 15
            if jogador_rect.left > self.rect.left:
                jogador_rect.left = self.rect.left - 15
            if jogador_rect.right > self.rect.right:
                jogador_rect.right = self.rect.right - 15
            if jogador_rect.right < self.rect.right:
                jogador_rect.right = self.rect.right + 15

    def desenhar(self):
        pygame.draw.line(tela, COR_PRETA, (self.rect.centerx, 0), (self.rect.centerx, ALTURA))