import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()

    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0
    fld = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        shot  = player.update(dt)
        if shot:
            shots.add(shot)

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisionCheck(shot):
                    asteroid.kill()
                    shot.kill()

        for asteroid in asteroids:
            if player.collisionCheck(asteroid):
                print("Game Over!")
                return
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()