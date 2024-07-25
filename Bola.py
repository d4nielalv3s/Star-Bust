import random
from Utils.Cores import *
from Utils.Telas import *

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(COR_AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA - 59, ALTURA / 2)
        dx_bola = (self.rect.x, self.rect.y)

    def pos_colisao(self, ia):
        if pygame.sprite.collide_rect(self, ia):
            self.rect.x = random.randint(0, LARGURA)
            self.rect.y = random.randint(0, ALTURA)