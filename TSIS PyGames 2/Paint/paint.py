import pygame, sys
import math
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

pygame.init()
sc = pygame.display.set_mode((800, 600))
check = True
check_draw = False
color = "white"
start_pos = (0, 0)
end_pps = (0, 0)
rect_flag = False
circle_flag = False
width_line = 2

eraser = pygame.image.load("E:\Учёба\PP2\TSIS PyGame 2\Paint\eraser.png")
eraser = pygame.transform.scale(eraser, (75, 75))

pygame.display.set_caption('paint')

while check:
    sc.blit(eraser, (350, 510))
    pygame.draw.rect(sc, (255, 255, 255), (480, 520, 60, 60))
    pygame.draw.circle(sc, (255, 255, 255), (620, 550), 35)
    pygame.draw.circle(sc, 'red', (50, 550), 25)
    pygame.draw.circle(sc, 'blue', (125, 550), 25)
    pygame.draw.circle(sc, 'green', (200, 550), 25)
    pygame.draw.circle(sc, 'white', (275, 550), 25)
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                check = False
        if rect_flag and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
        elif circle_flag and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            start_pos = event.pos
            check_draw = True


        if event.type == pygame.MOUSEMOTION:
            if check_draw:
                end_pos = event.pos
                pygame.draw.line(sc, color, start_pos, end_pos, width_line)
                start_pos = end_pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            check_draw = False
            if rect_flag:
                end_pos = event.pos
                x, y = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
                width_rect = max(end_pos[0], start_pos[0]) - x
                height_rect = max(end_pos[1], start_pos[1]) - y
                # sc.fill('black')
                pygame.draw.rect(sc, color, pygame.Rect(x, y, width_rect, height_rect))
            if circle_flag:
                end_pos = event.pos
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int(math.sqrt(dx ** 2 + dy ** 2)/2)
                cent = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                pygame.draw.circle(sc, color, cent, radius)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # print(event.pos)
            if 25 <= event.pos[0] <= 75 and 525 <= event.pos[1] <= 575:
                rect_flag = False
                circle_flag = False
                color = 'red'
                width_line = 2
            elif 100 <= event.pos[0] <= 150 and 525 <= event.pos[1] <= 575:
                rect_flag = False
                circle_flag = False
                color = "blue"
                width_line = 2
            elif 175 <= event.pos[0] <= 225 and 525 <= event.pos[1] <= 575:
                rect_flag = False
                circle_flag = False
                width_line = 2
                color = "green"
            elif 250 <= event.pos[0] <= 300 and 525 <= event.pos[1] <= 575:
                rect_flag = False
                circle_flag = False
                color = "white"
                width_line = 2
            elif 350 <= event.pos[0] <= 425 and 510 <= event.pos[1] <= 580:
                rect_flag = False
                circle_flag = False
                color = "black"
                width_line = 40
            elif 475 <= event.pos[0] <= 540 and 515 <= event.pos[1] <= 580:
                rect_flag = True
                check_draw = False
                circle_flag = False
            elif 585 <= event.pos[0] <= 655 and 510 <= event.pos[1] <= 585:
                rect_flag = False
                check_draw = False
                circle_flag = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            sc.fill(0)
    pygame.display.update()

pygame.quit()