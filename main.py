from player import *
import pygame

from constants import *


def main():
    pygame.init()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill scrren with black
        screen.fill("black")

        # draw player to screen
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # update graphics
        pygame.display.flip()
        
        # limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()