from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen,(255,255,255),(self.position.x,self.position.y),self.radius,2)

  def update(self,dt):
    self.position += self.velocity * dt

  def split(self):
    if(self.radius <= ASTEROID_MIN_RADIUS):
      self.kill()
      return
    else:
      spawn_angle = random.uniform(20,50)
      angle_a = self.velocity.rotate(spawn_angle)
      angle_b = self.velocity.rotate(-spawn_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      temp_a = Asteroid(self.position.x,self.position.y,new_radius)
      temp_a.velocity = angle_a * 1.2
      temp_b = Asteroid(self.position.x,self.position.y,new_radius)
      temp_b.velocity = angle_b * 1.2
      self.kill()

