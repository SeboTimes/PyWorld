import pygame

black = (0,0,0)
white = (255,255,255)
(width, height) = (800, 600)


screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Sebo hatn')
clock = pygame.time.Clock()

carImg = pygame.image.load("auto.jpeg")
backGroundImg = pygame.image.load("Hintergrund.jpg").convert()
enemyImg = pygame.image.load("Gegner.jpg")

screen.blit(backGroundImg, (0,0))

def car(x,y):
  screen.blit(carImg,(x,y))

vel = 10

x = (width * 0.45)
y = (height * 0.8)

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  keys  = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and x > 0:
    x -= vel
  
  if keys[pygame.K_RIGHT] and x < 800 - 270: #270 ist  die länge des autos
    x += vel
    
  screen.fill(black)

  car(x, y)
  pygame.display.update()
  screen.blit(carImg,(x,y))
  car(x,y)
  clock.tick(60)