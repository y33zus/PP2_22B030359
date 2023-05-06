import pygame

pygame.init()

# экран и имя
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("circle")

# переменные круга
circle_radius = 50
circle_x = 250
circle_y = 250

white = (255, 255, 255)
black = (130, 130, 130)

pygame.draw.circle(screen, black, (circle_x, circle_y), circle_radius)

pygame.display.update()

while True:
    # действия в игре
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                circle_y -= 20
            elif event.key == pygame.K_DOWN:
                circle_y += 20
            elif event.key == pygame.K_LEFT:
                circle_x -= 20
            elif event.key == pygame.K_RIGHT:
                circle_x += 20

            # условие не выхода
            if circle_x < circle_radius:
                circle_x = circle_radius
            elif circle_x > 500 - circle_radius:
                circle_x = 500 - circle_radius
            if circle_y < circle_radius:
                circle_y = circle_radius
            elif circle_y > 500 - circle_radius:
                circle_y = 500 - circle_radius

            # обнавление после движения
            screen.fill(white)
            pygame.draw.circle(screen, black, (circle_x, circle_y), circle_radius)
            pygame.display.update()
