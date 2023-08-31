from Scripts.Diplay import Display
from Scripts.Entity import Entity
from random import randint
import pygame

width, height = 800, 600

screen = Display((width, height))
screen.caption("PyWorld")
clock = pygame.time.Clock()

car = Entity("Images/auto.jpeg")
bomb = Entity("Images/Gegner.jpg")
bg = Entity("Images/Hintergrund.jpg")
bg.resize((width, height))

car.x = (width - car.getSize()[0]) / 2
car.y = (height - car.getSize()[1])

bomb.y = bomb.getSize()[1]

speed = 10

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  keys  = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and car.x > 0:
    car.x -= speed
  
  if keys[pygame.K_RIGHT] and car.x < width - 270: #270 ist  die länge des autos
    car.x += speed

  screen.render(bg)
  screen.render(car)
  screen.render(bomb)

  if bomb.y > height - bomb.getSize()[1]:
    bomb.y = -bomb.getSize()[1]
    bomb.x = randint(0, width - car.getSize()[0])
  else:
    bomb.y += speed / 2

  if car.isTouching(bomb):
    screen.fill((255, 0, 0)) 

  screen.update()
  clock.tick(60)