import pygame
from asteroid import *
from asteroidfield import AsteroidField
from player import *
from constants import *



def main():
    pygame.init()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # logic timing / screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # asteroids
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill scrren with black
        screen.fill("black")

        # update inputs and game logic
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # update graphics to screen
        pygame.display.flip()
        
        # limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()