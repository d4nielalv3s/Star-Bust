import math
from Utils.Cores import *
from Utils.Telas import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(COR_VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA - 60, ALTURA / 2)

    def movimentacao(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 14
        if keys[pygame.K_d]:
            self.rect.x += 14
        if keys[pygame.K_s]:
            self.rect.y += 14
        if keys[pygame.K_w]:
            self.rect.y -= 14

    def agarrar(self, bola):
        dx = self.rect.x - bola.rect.x
        dy = self.rect.y - bola.rect.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        limite_distancia = 50

        if distancia <= limite_distancia:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                deslocamento_x = 20
                bola.rect.centerx = self.rect.centerx + deslocamento_x
                bola.rect.centery = self.rect.centery

    # def colisao_arremesso(self, bola):
    #     dx_jogador = bola.rect.x - self.rect.x
    #     dy_jogador = bola.rect.y - self.rect.y
    #
    #     if self.rect.colliderect(bola.rect):
    #         forca_arremesso = 20
    #         angulo = math.atan2(dy_jogador, dx_jogador)
    #         velocidade_horizontal = forca_arremesso * math.cos(angulo)
    #         bola.rect.x -= int(velocidade_horizontal)
    #         bola.rect.x = random.randint(0, LARGURA // 2 - bola.rect.width)
    #         bola.rect.y = random.randint(0, ALTURA - bola.rect.height)

    def colisao_arremesso(self, bola):
        dx_jogador = bola.rect.x - self.rect.x
        dy_jogador = bola.rect.y - self.rect.y

        if self.rect.colliderect(bola.rect):
            forca_arremesso = 20

            if abs(dx_jogador) > abs(dy_jogador):
                velocidade_horizontal = forca_arremesso if dx_jogador > 0 else -forca_arremesso
                bola.rect.x += int(velocidade_horizontal)
            else:
                velocidade_vertical = forca_arremesso if dy_jogador > 0 else -forca_arremesso
                bola.rect.y += int(velocidade_vertical)

            bola.rect.x = max(0, min(bola.rect.x, LARGURA - bola.rect.width))
            bola.rect.y = max(0, min(bola.rect.y, ALTURA - bola.rect.height))