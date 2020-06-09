import pygame

SIZE = WIDTH, HEIGHT = 640, 480

pygame.init()
screen = pygame.display.set_mode(SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
