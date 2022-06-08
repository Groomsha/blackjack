from typing import Dict

import pygame

from players.player import Player
from players.dealer import Dealer


class Game:
	FPS: int = 30
	WIDTH: int = 800
	HEIGHT: int = 600

	def __init__(self, settings: Dict) -> None:
		pygame.init()
		self.clock = pygame.time.Clock()

		pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({settings.get("description")}) {settings.get("version_app")}')

		self.player = Player()
		self.dealer = Dealer()

		self.main_game_loop()

	def main_game_loop(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

			self.clock.tick(self.FPS)
