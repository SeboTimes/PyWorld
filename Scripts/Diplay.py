from Scripts.Entity import Entity
import pygame

class Display:
    def __init__(self, resulution: tuple):
        self._surface = pygame.display.set_mode(resulution, pygame.RESIZABLE)
        pygame.display.flip()

    def setResolution(self, resolution: tuple):
        self._surface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
        pygame.display.flip()
    
    def getResolution(self) -> tuple:
        return self._surface.get_size()

    def caption(self, caption: str):
        pygame.display.set_caption(caption)
        pygame.display.flip()

    def update(self):
        pygame.display.update()
    
    def fill(self, color: tuple):
        self._surface.fill(color)
    
    def render(self, entity: Entity):
        self._surface.blit(entity._surface, (entity.x, entity.y))
