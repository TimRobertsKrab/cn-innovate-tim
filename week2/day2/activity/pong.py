from pdb import Restart
import pygame, sys, random 

pygame.init()

clock = pygame.time.Clock()

screen_width = 1000
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("PONG")

ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)
bg_color = pygame.Color("grey12")
light_grey = (200,200,200)

ball_colour = light_grey

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))

player_speed_x = 0
player_speed_y = 0
player_speed_x_increment = 3
player_speed_y_increment = 6

opponent_speed = 7

ball_coordinates = [[None]*2 for i in range(5)]

normalised_speed = 49.0/(98**0.5)


def ball_animation():
    global ball_speed_x,ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_width or ball.left <= 0:
        ball_restart()

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y+=player_speed_y
    player.x+=player_speed_x

    if player.right > screen_width - 10:
        player.right = screen_width-10

    if player.left < screen_width/2:
        player.left = screen_width/2

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.centery < ball.centery:
        opponent.centery += opponent_speed
    if opponent.centery > ball.centery:
        opponent.centery -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_restart():
    global ball_speed_x,ball_speed_y

    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed_y += player_speed_y_increment
            if event.key == pygame.K_UP:
                player_speed_y -= player_speed_y_increment
            if event.key == pygame.K_LEFT:
                player_speed_x -= player_speed_x_increment
            if event.key == pygame.K_RIGHT:
                player_speed_x += player_speed_x_increment

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed_y -= player_speed_y_increment
            if event.key == pygame.K_UP:
                player_speed_y += player_speed_y_increment
            if event.key == pygame.K_LEFT:
                player_speed_x += player_speed_x_increment
            if event.key == pygame.K_RIGHT:
                player_speed_x -= player_speed_x_increment
        
    # Animation
    ball_animation()
    player_animation()
    opponent_animation()
    # Draw
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,ball_colour,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()

    clock.tick(60)
