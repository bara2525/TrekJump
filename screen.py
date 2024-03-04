import pygame
screen = pygame.display.set_mode((1000, 1000))

class deathScreen:
    def __init__(self,coordinates_x, coordinates_y):
        self.clicked = False
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y
    def draw(self):
        new = pygame.font.Font("img/Star Trek_future.ttf", 100)
        img1 = new.render('You died', True, (250, 200, 73))
        screen.blit(img1, (380, 250))
        new = pygame.font.Font("img/Star Trek_future.ttf", 50)
        img2 = new.render('Press R for Restart', True, (250, 200, 73))
        screen.blit(img2, (350, 600))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.clicked = True
            return self.clicked
        else :
            self.clicked = False
            return False
class starScreen:
    def __init__(self):
        self.background = pygame.image.load("img/background2.jpg")
    def draw(self):
        self.star_screen = pygame.transform.scale(self.background,(1000,1000))
        screen.blit(self.star_screen, (0,0))

        name = pygame.font.Font("img/Star Trek_future.ttf", 200)
        img1 = name.render('TREK JUMP', True, (250, 200, 73))
        screen.blit(img1, (217, 100))

        new = pygame.font.Font("img/Star Trek_future.ttf",100)
        img2 = new.render('START', True, (250, 200, 73))
        width = img2.get_width()
        pygame.draw.rect(screen, (233,24,250), (390, 450, 220, 100),5)
        screen.blit(img2, (500 - width // 2, 440))

        if 390 < pygame.mouse.get_pos()[0] < 610:
            if 450 < pygame.mouse.get_pos()[1] < 550:
                if  pygame.mouse.get_pressed()[0]:
                    return True

class exitScreen:
    def __init__(self):
        self.background = pygame.image.load("img/background2.jpg")
    def draw(self, coin):
        self.exit_screen = pygame.transform.scale(self.background,(1000,1000))
        screen.blit(self.exit_screen, (0, 0))
        new = pygame.font.Font("img/Star Trek_future.ttf", 100)
        img = new.render('KONEC HRY', True, (250, 200, 73))
        width = img.get_width()
        pygame.draw.rect(screen, (233, 24, 250), (345, 450, width+20, 100), 5)
        screen.blit(img, (500 - width // 2, 440))
        img1 = new.render("COINS: " + str(coin), True, (250, 200, 73))
        screen.blit(img1, (400,600))
        if 390 < pygame.mouse.get_pos()[0] < 610:
            if 450 < pygame.mouse.get_pos()[1] < 550:
                if  pygame.mouse.get_pressed()[0]:
                    self.nothing = False
                    return True