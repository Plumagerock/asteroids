import pygame
from player import *
from shot import *
from asteroid import *
from asteroidfield import *
from constants import *



def main():
    pygame.init()

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # logic timing / screen
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    # game loop start
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

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                # end game
                pygame.quit()
                print("Game over!")

        # update graphics to screen
        pygame.display.flip()
        
        # limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()