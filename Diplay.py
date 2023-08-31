import pygame

class Display:
    screen: pygame.Surface

    def __init__(self, resulution: tuple):
        self.screen = pygame.display.set_mode(resulution)
        pygame.display.flip()

    def resulution(self, resulution: tuple):
        self.screen = pygame.display.set_mode(resulution)
        pygame.display.flip()

    def caption(self, caption: str):
        pygame.display.set_caption(caption)
        pygame.display.flip()

    def update(self):
        pygame.display.update()
    
    def fill(self, color: tuple):
        self.screen.fill(color)
    
    def render(self, entity: pygame.Surface, size: tuple):
        self.screen.blit(entity, size)
