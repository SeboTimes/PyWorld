import pygame

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Sebo hatn kleinen')
background_colour = (255,255,255)
screen.fill(background_colour)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False