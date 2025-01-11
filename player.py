from circleshape import CircleShape
from constants import *
from shot import *
import pygame

class Player(CircleShape):
  def __init__(self,x,y):
    super().__init__(x,y,PLAYER_RADIUS)
    self.rotation = 0
    self.shot_timer = 0

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

  def update(self,dt):
    self.rotate(dt)
    self.move(dt)
    self.shoot()
    self.shot_timer -= dt

  def rotate(self,dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
      self.rotation += PLAYER_TURN_SPEED * dt
    if keys[pygame.K_a]:
      self.rotation -= PLAYER_TURN_SPEED * dt
  
  def move(self,dt):
    keys = pygame.key.get_pressed()
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    if keys[pygame.K_w]:
      self.position += forward * PLAYER_SPEED * dt
    if keys[pygame.K_s]:
      self.position -= forward * PLAYER_SPEED * dt
  
  def shoot(self):
    if(self.shot_timer > 0):
      return
    
    keys = pygame.key.get_pressed()
    forward = pygame.Vector2(0, 1).rotate(self.rotation)

    if keys[pygame.K_SPACE]:
      Shot(self.position.x,self.position.y,forward*PLAYER_SHOOT_SPEED)
      self.shot_timer = PLAYER_SHOT_COOLDOWN
