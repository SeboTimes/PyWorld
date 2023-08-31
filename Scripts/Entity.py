from typing import Self
import pygame

class Entity:
    def __init__(self, image: str):
        self.surface = pygame.image.load(image)
        self.x = 0
        self.y = 0

    def resize(self, size: tuple):
        self.surface = pygame.transform.scale(self.surface, size)
    
    #def isColliding(self, entity: Self):
    #    return entity.surface.get_rect().collidelist()

    def getSize(self):
        return self.surface.get_size()
