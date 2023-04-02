import pygame

pygame.init()

screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 44)

music_list = ["E:\Учёба\PP2\TSIS PyGame\Music Player\Pesnya1.mp3", "E:\Учёба\PP2\TSIS PyGame\Music Player\Pesnya2.mp3", "E:\Учёба\PP2\TSIS PyGame\Music Player\Pesnya3.mp3"]
current_index = 0

pygame.mixer.init()
pygame.mixer.music.load(music_list[current_index])
playing = False

screen.fill((255, 255, 255))
text = font.render("Press SPACE to play/pause, LEFT/RIGHT to change the song", True, (0, 0, 0))
screen.blit(text, (20, 20))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_LEFT:
                current_index -= 1
                if current_index < 0:
                    current_index = len(music_list) - 1
                pygame.mixer.music.load(music_list[current_index])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_RIGHT:
                current_index += 1
                if current_index >= len(music_list):
                    current_index = 0
                pygame.mixer.music.load(music_list[current_index])
                pygame.mixer.music.play()
                playing = True

    screen.fill((255, 255, 255))
    text = font.render("Press SPACE to play/pause, LEFT/RIGHT to skip", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    pygame.display.update()
