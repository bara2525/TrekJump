import pygame
screen = pygame.display.set_mode((1000, 1000))
class coin:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
        self.allow = True
    def draw(self):
        self.coin = pygame.image.load("img/coin.png")
        if self.visible:
            screen.blit(self.coin, (self.x * 50, self.y * 50))
    def remove(self):
        self.x = 0
        self.y = 0

class key:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        self.key = pygame.image.load("img/key.png")
        screen.blit(self.key, (self.x * 50, self.y * 50))
    def inventory(self):
        self.key = pygame.image.load("img/key.png")
        pygame.draw.rect((screen), (158, 158, 158), (50, 100, 50, 50))
        screen.blit(self.key, (50, 100))