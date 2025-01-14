# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *


def game_loop(screen, clock, player, updatable, drawable, asteroids, shots):
	while True:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		dt = clock.tick(60) / 1000
		updatable.update(dt)

		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game Over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:	
				if shot.collision(asteroid):
					asteroid.split()
					shot.kill()

		screen.fill((0, 0, 0))

		for sprite in drawable:
			sprite.draw(screen)
			
		player.draw(screen)  # Custom draw for Player
		pygame.display.flip()

def main():
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable,)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable,)

	pygame.init()
	clock = pygame.time.Clock()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	# initialize elements
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2, updatable)
	asteroid_field = AsteroidField()
	total_shots = []
	
	game_loop(screen, clock, player, updatable, drawable, asteroids, shots)


if __name__ == "__main__":
    main()
