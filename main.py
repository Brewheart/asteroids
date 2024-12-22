# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

def game_loop(screen, clock, player):
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		time_passed = clock.tick(60) / 1000
		update_game(time_passed) 

		screen.fill((0, 0, 0))
		player.draw(screen)
		pygame.display.flip()

def main():
	pygame.init()
	clock = pygame.time.Clock()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	game_loop(screen, clock, player)


def update_game(delta_time):
	#move_player(delta_time)
	pass

if __name__ == "__main__":
    main()
