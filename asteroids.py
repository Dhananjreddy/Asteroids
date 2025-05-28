import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = pygame.Vector2(0,0)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius)

  def update(self, dt):
    self.position += self.velocity * dt
