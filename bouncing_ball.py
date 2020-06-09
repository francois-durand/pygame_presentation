# Adapted from https://fr.wikibooks.org/wiki/Pygame/Introduction_%C3%A0_Pygame
import pygame

SIZE = WIDTH, HEIGHT = 640, 480
BLACK = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

ball = pygame.image.load("ball.gif").convert_alpha()
ball_rect = ball.get_rect()
ball_speed = [2, 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_rect.move_ip(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
        ball_speed[1] = -ball_speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(100)
