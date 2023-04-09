import pygame, sys
import time
import random

from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

snake_speed = 30
speed = 10
WIDTH = 720
HEIGHT = 480
#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.init()
pygame.display.set_caption('TiSoft snake')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
#FPS controller
fps = pygame.time.Clock()
#snake default pos
snake_position = [100, 50]
 
#first 4 blocks of snake's body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
#fruit pos
fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                  random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True #default food spawning 
#default snake direction
direction = 'RIGHT'
change_to = direction

level = 1
score = 0
 #show score obvi
def show_score(choice, color, font, size):
    #creating where score will be displayed
    score_font = pygame.font.SysFont(font, size)
    #create the display surface object
    score_surface = score_font.render('Score : ' + str(score), True, color)
    #rect for score
    score_rect = score_surface.get_rect()
    #text
    game_window.blit(score_surface, score_rect)
#show level obvi
def show_level(choice, color, font, size):
    #creating where score will be displayed
    level_font = pygame.font.SysFont(font, size)
    #create the display surface object
    level_surface = level_font.render('Level : ' + str(level), True, color)
    #text
    game_window.blit(level_surface, (0,25))
#if we lose game
def game_over():
    pygame.display.flip()
    #quit after 2secs
    time.sleep(1)
    pygame.quit()
    quit()

#game loop
while True:
    # handling key events
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    #giving commands 2move
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= speed
    if direction == 'DOWN':
        snake_position[1] += speed
    if direction == 'LEFT':
        snake_position[0] -= speed
    if direction == 'RIGHT':
        snake_position[0] += speed

    food_timer=1
    points = [10,20,30,40]
    speeds = {100:[15,2],
              200:[20,3],
              300:[25,4]}
 
    #collision while eating fruit
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += random.choice(points)
        fruit_spawn = False
        food_timer = 0
        for i in speeds:
            if score >= i:
                snake_speed = speeds[i][0]
                level = speeds[i][1]
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
    if food_timer > 5:
        food_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True
        food_timer = 0

     
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
 
    #if snake collides w// screen's ending
    if snake_position[0] < 0 or snake_position[0] > WIDTH-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        game_over()
     
    #if snake touches its body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    #score displayed
    show_score(1, white, 'times new roman', 30)
    show_level(1, white, 'times new roman', 30)
     
    #updating game screen
    pygame.display.update()
    #rate of screen update
    fps.tick(snake_speed)