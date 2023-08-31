import pygame

screen: pygame.Surface

class Display:
    def __init__(self, width: int, height: int):
        screen = pygame.display.set_mode((width, height))
        pygame.display.flip()
        pygame.display.set_caption('Sebo hatn kleinen')
        background_colour = (255,255,255)
        screen.fill(background_colour)

    def resulution(width, height):
        screen = pygame.display.set_mode((width, height))
        pygame.display.flip()

    def update():
        pygame.display.update()
