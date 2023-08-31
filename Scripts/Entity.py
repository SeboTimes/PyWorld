from typing import Self
import pygame

class Entity:
    def __init__(self, image: str):
        self.surface = pygame.image.load(image)

    def resize(self, size: tuple):
        self.surface = pygame.transform.scale(self.surface, size)
    
    def getSize(self):
        return self.surface.get_size()
