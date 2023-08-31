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

car.x = (width - car.getSize()[0]) / 2
car.y = (height - car.getSize()[1])

bomb.y = bomb.getSize()[1]

speed = 10

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  (width, height) = screen.getResolution()

  keys  = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and car.x > 0:
    car.x -= speed
  
  if keys[pygame.K_RIGHT] and car.x < width - car.getSize()[0]:
    car.x += speed
  elif car.x > width - car.getSize()[0]:
    car.x = width - car.getSize()[0]

  screen.render(Entity("Images/Hintergrund.jpg").resize(screen.getResolution()))
  car.y = (height - car.getSize()[1])
  screen.render(car)
  screen.render(bomb)

  if bomb.y > height - bomb.getSize()[1]:
    bomb.x = car.x
    bomb.y = -bomb.getSize()[1]
    speed += 1
  else:
    bomb.y += speed / 2

  if car.isTouching(bomb):
    bomb.x = randint(0, width - car.getSize()[0])
    bomb.y = -bomb.getSize()[1]
    speed -= 1
    screen.fill((255, 0, 0))

  screen.update()
  clock.tick(60)