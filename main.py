from player import *
import pygame

from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill scrren with black
        screen.fill("black")

        # draw player to screen
        player.update(dt)
        player.draw(screen)

        # update graphics
        pygame.display.flip()
        
        # limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()