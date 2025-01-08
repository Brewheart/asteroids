# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Player.containers = (updatable, drawable)



def game_loop(screen, clock):
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		dt = clock.tick(60) / 1000
		updatable.update(dt)

		screen.fill((0, 0, 0))
		drawable.draw(screen)
		pygame.display.flip()

def main():
	pygame.init()
	clock = pygame.time.Clock()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	game_loop(screen, clock)


if __name__ == "__main__":
    main()
