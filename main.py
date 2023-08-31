from Diplay import Display
import pygame

black = (0,0,0)
white = (255,255,255)
resulution = (800, 600)

screen = Display(resulution)
screen.caption("PyWorld")
clock = pygame.time.Clock()

carImg = pygame.image.load("auto.jpeg")
backGroundImg = pygame.image.load("Hintergrund.jpg")
backGroundImg = pygame.transform.scale(backGroundImg, resulution)
enemyImg = pygame.image.load("Gegner.jpg")

def car(x, y):
  screen.render(carImg, x, y)

vel = 10

x = (resulution[0] * 0.5)
y = (resulution[1] * 0.5)

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
  screen.render(backGroundImg, 0, 0)

  car(x, y)
  pygame.display.update()
  screen.render(carImg, x, y)
  clock.tick(60)