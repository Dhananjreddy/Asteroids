import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    rand_angle = random.uniform(20,50)
    new_velocity_1 = self.velocity.rotate(rand_angle)
    new_velocity_2 = self.velocity.rotate(-rand_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_1.velocity = new_velocity_1 * 1.2
    asteroid_2.velocity = new_velocity_2 * 1.2
    

class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = pygame.Vector2(0,0)
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius)

  def update(self, dt):
    self.position += self.velocity * dt
