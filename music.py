import pygame
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 1000))
jump_sound = pygame.mixer.Sound("sound/jump.wav")
lava_sound = pygame.mixer.Sound("sound/game_over.wav")
transport_sound = pygame.mixer.Sound("sound/transport.mp3")
music = pygame.mixer.music.load("sound/music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)