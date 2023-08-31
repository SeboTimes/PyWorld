import pygame

black = (0,0,0)
white = (255,255,255)
(width, height) = (800, 600)


screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Sebo hatn')
screen.fill(black)
clock = pygame.time.Clock()

carImg = pygame.image.load("auto.jpeg")

def car(x,y):
  screen.blit(carImg,(x,y))

x = (width * 0.45)
y = (height * 0.8)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  screen.fill(white)
  car(x, y)
  pygame.display.update()
  car(x,y)
  clock.tick(60)