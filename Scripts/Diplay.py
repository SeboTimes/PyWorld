from Scripts.Entity import Entity
import pygame

class Display(object):
    def __init__(self, resulution: tuple):
        self.surface = pygame.display.set_mode(resulution)
        pygame.display.flip()

    def resulution(self, resulution: tuple):
        self.surface = pygame.display.set_mode(resulution)
        pygame.display.flip()

    def caption(self, caption: str):
        pygame.display.set_caption(caption)
        pygame.display.flip()

    def update(self):
        pygame.display.update()
    
    def fill(self, color: tuple):
        self.surface.fill(color)
    
    def render(self, entity: Entity):
        self.surface.blit(entity.surface, (entity.x, entity.y))
