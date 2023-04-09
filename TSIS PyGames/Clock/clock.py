import pygame, sys, datetime

def rot_center(image, angle, x, y):
    rotated_img = pygame.transform.rotate(image, angle)
    new_rect = rotated_img.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_img, new_rect

pygame.init()

display = pygame.display.set_mode((800, 600))

back = pygame.image.load('E:\Учёба\PP2\TSIS PyGame\Clock\clock.jpg')
minute_hand = pygame.image.load('E:\Учёба\PP2\TSIS PyGame\Clock\minutes.jpg')
seconds_hand = pygame.image.load('E:\Учёба\PP2\TSIS PyGame\Clock\seconds.jpg')

back = pygame.transform.scale(back, (800, 600))
minute_hand = pygame.transform.scale(minute_hand, (300, 300))
seconds_hand = pygame.transform.scale(seconds_hand, (300, 300))

while True:

    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x = (-6*min)%360
    y = ((-1)*sec * 6)%360

    rot_right, x = rot_center(minute_hand, x, 400, 300)
    rot_left, y = rot_center(seconds_hand, y, 400, 300)

    display.blit(back, (0, 0))
    #display.blit(rot_right, x)
    display.blit(rot_left, y)

    pygame.display.update()