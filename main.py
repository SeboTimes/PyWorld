from Scripts.Diplay import Display
from Scripts.Entity import Entity
import pygame

black = (0,0,0)
white = (255,255,255)
width, height = 800, 600

screen = Display((width, height))
screen.caption("PyWorld")
clock = pygame.time.Clock()

car = Entity("Images/auto.jpeg")
bomb = Entity("Images/Gegner.jpg")
bg = Entity("Images/Hintergrund.jpg")
bg.resize((width, height))

vel = 10

x = (width - car.getSize()[0]) / 2
y = (height - car.getSize()[1])

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  keys  = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and x > 0:
    x -= vel
  
  if keys[pygame.K_RIGHT] and x < width - 270: #270 ist  die länge des autos
    x += vel

  screen.render(bg, (0, 0))

  screen.render(car, (x, y))
  screen.update()
  clock.tick(60)