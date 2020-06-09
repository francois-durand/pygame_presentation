import pygame

SIZE = WIDTH, HEIGHT = 640, 480
BLACK = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

box_empty = pygame.image.load("box.gif").convert_alpha()
box = box_empty.copy()
box_rect = box.get_rect()
speed_box = [2, 2]

ball = pygame.image.load("ball.gif").convert_alpha()
ball_rect = ball.get_rect()
speed_ball = [1, 1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box_rect.move_ip(speed_box)
    if box_rect.left < 0 or box_rect.right > WIDTH:
        speed_box[0] = -speed_box[0]
    if box_rect.top < 0 or box_rect.bottom > HEIGHT:
        speed_box[1] = -speed_box[1]

    ball_rect.move_ip(speed_ball)
    if ball_rect.left < 0 or ball_rect.right > box_rect.width:
        speed_ball[0] = -speed_ball[0]
    if ball_rect.top < 0 or ball_rect.bottom > box_rect.height:
        speed_ball[1] = -speed_ball[1]

    box.blit(box_empty, (0, 0))
    box.blit(ball, ball_rect)

    screen.fill(BLACK)
    screen.blit(box, box_rect)
    pygame.display.update()
    clock.tick(100)
