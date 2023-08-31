from typing import Self
import pygame

class Entity:
    def __init__(self, image: str):
        self._surface = pygame.image.load(image)
        self._rect = self._surface.get_rect()
        self.x = 0
        self.y = 0

    def resize(self, size: tuple) -> Self:
        self._surface = pygame.transform.scale(self._surface, size)
        return self

    def getSize(self) -> tuple:
        return self._surface.get_size()
    
    def isTouching(self, entity: Self) -> bool:
        self._rect.center = (self.x, self.y)
        entity._rect.center = (entity.x, entity.y)
        return self._rect.colliderect(entity._rect)
