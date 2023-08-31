import pygame

class Display:
    screen: pygame.Surface

    def __init__(self, width: int, height: int):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.flip()

    def resulution(self, width: int, height: int):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.flip()

    def caption(self, caption: str):
        pygame.display.set_caption(caption)
        pygame.display.flip()

    def update(self):
        pygame.display.update()
    
    def fill(self, color: tuple):
        self.screen.fill(color)
    
    def render(self, entity: pygame.Surface, x: float, y:float):
        self.screen.blit(entity, (x,y))
