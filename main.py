import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

from shot import *

import sys


def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  pygame.init()
  Asteroid.containers = (asteroids, updatable, drawable)
  Player.containers = (updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  asteroid_field = AsteroidField()

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  clock = pygame.time.Clock()
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

      for sprite in updatable:
          sprite.update(dt)

      for asteroid in asteroids:
          if player.is_colliding(asteroid):
              print("Game over!")
              sys.exit()
          for shot in shots:
              if shot.is_colliding(asteroid):
                  asteroid.split()
                  shot.kill()

      screen.fill((0, 0, 0))

      for sprite in drawable:
          sprite.draw(screen)

      pygame.display.flip()
      dt = clock.tick(60)/1000


if __name__ == "__main__":
  main()
