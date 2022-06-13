import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("PONG")

ball = pygame.Rect(screen_width/2,screen_height/2,30,30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    clock.tick(60)
