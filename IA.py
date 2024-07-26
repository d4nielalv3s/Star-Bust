import random
import math
from Utils.Cores import *
from Utils.Telas import *

class IA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(COR_VERMELHA)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA / 10, ALTURA / 2)
        self.velocidade = 10

    def movimentacao_ia(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10

        variacao_de_velocidade = [0.2, 0.3, 0.4]
        escolha_de_variacao = random.choice(variacao_de_velocidade)
        pygame.time.delay(int(escolha_de_variacao * 100))

    def persequir(self, bola):
        variacao_de_velocidade = [0.2, 0.3, 0.4]
        escolha_de_variacao = random.choice(variacao_de_velocidade)
        pygame.time.delay(int(escolha_de_variacao * 100))
        if self.rect.x < bola.rect.x:
            self.rect.x += 10
        elif self.rect.x > bola.rect.x:
            self.rect.x -= 10
        if self.rect.y < bola.rect.y:
            self.rect.y += 10
        elif self.rect.y > bola.rect.y:
            self.rect.y -= 10
