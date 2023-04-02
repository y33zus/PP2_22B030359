import pygame
import random

# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

def select_color(key):
    global color
    if key == pygame.K_r:
        color = (255, 0, 0) # Red
    elif key == pygame.K_g:
        color = (0, 255, 0) # Green
    elif key == pygame.K_b:
        color = (0, 0, 255) # Blue
    elif key == pygame.K_e:
        color = (255, 255, 255) # White (Eraser)

def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)


try :
    while True :
        e = pygame.event.wait()

        if e.type == pygame.QUIT :
            raise StopIteration
        if e.type == pygame.KEYDOWN:
            select_color(e.key)

        if e.type == pygame.MOUSEBUTTONDOWN :
            # Selecting random Color Code
            color = (random.randrange(256), random.randrange(
                256), random.randrange(256))
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # Draw a single circle wheneve(mouse is clicked down.
        pygame.draw.circle(screen, color, e.pos, radius)
        draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION :
            if draw_on :
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration :
    pass

# Quit
pygame.quit()