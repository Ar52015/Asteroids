import pygame
from circleshape import *
from constants import *
from shot import *
import time

global_last_shot_time = 0

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            shot = self.shoot()
            if shot:
                return shot

    def shoot(self):
        global global_last_shot_time
        current_time = time.time()
        if current_time - global_last_shot_time >= SHOT_COOLDOWN:
            self.last_shot_time = current_time
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            position = self.position + forward * self.radius
            global_last_shot_time = current_time
            return Shot(position.x, position.y, SHOT_RADIUS, self.rotation)
        return None