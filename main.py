import pygame
from pygame.locals import *
from screen import starScreen
from screen import exitScreen
from screen import deathScreen
from maps import world_map, pictures_of_background
from collect import coin, key
from music import jump_sound, lava_sound, transport_sound, music

pygame.init()
clock = pygame.time.Clock()
window_width = 1000
window_height = 1000
pygame.display.set_caption("Trek Jump")
screen = pygame.display.set_mode((1000, 1000))


class Platform:
    def __init__(self, map):
        grass = pygame.image.load("img/Marble.png")
        self.grass = pygame.transform.scale(grass, (50, 50))
        self.maps = map
        self.list = []
        self.visibility = True
        self.lava = pygame.image.load("img/lava.png")
        self.key = pygame.image.load("img/key.png")

    def draw(self):
        y = 0
        for row in self.maps:
            x = 0
            for tile in row:
                if tile == 1:
                    screen.blit(self.grass, (x * 50, y * 50))
                    img_rect = self.grass.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (self.grass, img_rect)
                    self.list.append(img_with_rect)

                if tile == 2:
                    screen.blit(self.lava, (x * 50, y * 50))
                    img_rect = self.lava.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (2, img_rect)
                    self.list.append(img_with_rect)

                if tile == 3:
                    img_rect = self.key.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (3, img_rect)
                    self.list.append(img_with_rect)
                    keys = key(x, y)
                    if not player.have_key:
                        keys.draw()
                    else:
                        keys.inventory()

                if tile == 5:
                    self.coin = pygame.image.load("img/coin.png")
                    img_rect = self.coin.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (5, img_rect)
                    self.list.append(img_with_rect)

                    coins = coin(x, y, self.visibility)

                    if player.show_coin:
                        coins.draw()

                if tile == 8:
                    self.door = pygame.image.load("img/door.png")
                    screen.blit(self.door, (x * 50, y * 50))
                    img_rect = self.grass.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (8, img_rect)
                    self.list.append(img_with_rect)

                if tile == 9:
                    self.door = pygame.image.load("img/door1.png")
                    screen.blit(self.door, (x * 50, y * 50))
                    img_rect = self.grass.get_rect()
                    img_rect.x = x * 50
                    img_rect.y = y * 50
                    img_with_rect = (9, img_rect)
                    self.list.append(img_with_rect)
                x += 1
            y += 1


class Player:
    def __init__(self, x, y, money):
        player_img = pygame.image.load("img/spock1.png")
        self.reset = False
        self.image = player_img
        self.player_right = [pygame.image.load("img/spock1.png"),
                             pygame.image.load("img/spock2.png"),
                             pygame.image.load("img/spock3.png"),
                             pygame.image.load("img/spock4.png")]

        self.player_left = []
        self.index = 0
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        for i in range(0, 4):
            self.player_left.append(pygame.transform.flip(self.player_right[i], True, False))
        self.stop_moving = False
        # vpravo
        self.new_map = False
        self.speed_up = 0
        self.rect.x = x
        self.rect.y = y
        self.way = 0
        self.gravity_counter = 100
        self.can_collect = True
        self.fall = True
        self.velocity = 7
        self.negative = -1
        self.coins = money
        self.show_coin = True
        self.counter = 0
        self.tell = 0
        self.have_key = False

    def draw(self):
        self.dx = 0
        self.dy = 0
        self.jumped = False

        pygame.draw.rect(screen, (158, 158, 158), (50, 50, 150, 50))
        name = pygame.font.Font("img/Star Trek_future.ttf", 45)
        img1 = name.render(f'Coins: {self.coins}', True, (0, 0, 0))
        screen.blit(img1, (75, 50))

        if not self.stop_moving:

            keys = pygame.key.get_pressed()
            # stisknutí levé šipky + pohyb
            if keys[pygame.K_LEFT] and self.rect.x > self.velocity - 10:
                self.dx -= self.velocity
                self.way = 1
                self.counter += 1

                # stisknutí pravé šipky + pohyb
            if keys[pygame.K_RIGHT] and self.rect.x < window_width - 55:
                self.dx += self.velocity
                self.way = -1
                self.counter += 1

                # není stisknuto nic
            if keys[pygame.K_LEFT] is False and keys[pygame.K_RIGHT] is False:
                self.counter = 0
                self.index = 0

                if self.way == -1:
                    self.image = self.player_right[self.index]
                if self.way == 1:
                    self.image = self.player_left[self.index]

            if self.jumped is False:
                if keys[pygame.K_SPACE] and self.fall is False and self.can_jump is False:
                    self.speed_up = -15
                    jump_sound.play()

                if keys[pygame.K_SPACE] is False:
                    self.speed_up += 1
        self.speed_up += 1
        if self.speed_up > 10:
            self.speed_up = 10

        self.dy += self.speed_up

        if self.rect.bottom > 985:
            self.rect.bottom = 985

        self.jumped = True
        self.fall = False
        if self.counter > 5:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.player_right):
                self.index = 0
            if self.way == -1:
                self.image = self.player_right[self.index]
            if self.way == 1:
                self.image = self.player_left[self.index]

        self.can_jump = True

        for tile in platform.list:

            if (tile[0] == 2) and (
                    tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height)
                    or tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height)):

                death = deathScreen(self.rect.x, self.rect.y)
                self.stop_moving = True
                if death.draw():
                    self.reset = True
                    self.stop_moving = False
                    lava_sound.play()

                # check collision with door
            elif (tile[0] == 3) and (
                    tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height)
                    or tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height)):
                self.have_key = True

            elif (tile[0] == 5) and (
                    tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height)
                    or tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height)):
                if self.can_collect is True:
                    self.coins += 1
                    self.can_collect = False
                    self.show_coin = False

            elif (tile[0] == 8 or tile[0] == 9) and (
                    tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height)
                    or tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height)):
                self.new_map = True
                self.can_collect = True
                if self.have_key is True:
                    transport_sound.play()
                    return self.new_map

                # check collision y
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height) and tile[0] != 5 and \
                    tile[0] != 3:
                # jumping
                if self.speed_up < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    # block above
                elif self.speed_up >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.can_jump = False

                    # check collision x
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height) and tile[0] != 5 and \
                    tile[0] != 3:
                self.dx = 0

        self.rect.y += self.dy
        self.rect.x += self.dx
        if self.reset is True:
            self.rect.y = 800
            self.rect.x = 100
            screen.blit(self.image, self.rect)
            self.reset = False
        else:
            screen.blit(self.image, self.rect)


# instance obrazovek
starScreen1 = starScreen()
exitScreen1 = exitScreen()
# player
player = Player(100, 950, 0)
level = 0
# prvni uroven
platform = Platform(world_map[level])

running = True
play = True
exit_game = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if exit_game is True and (starScreen1.draw() or play is False):
        if level < len(pictures_of_background):
            screen.blit(pictures_of_background[level], [0, 0])
        platform.draw()
        if player.draw():
            level += 1
            player = Player(100, 950, player.coins)
            player.draw()
            screen.blit(pictures_of_background[level], [0, 0])
            if level < len(world_map):
                platform = Platform(world_map[level])
            else:
                exit_game = False
        play = False

    if exit_game is False:
        if exitScreen1.draw(player.coins):
            running = False

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
