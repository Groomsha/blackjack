#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

"""
Project Name: 'BlackJack'
Description: Створення гри BlackJack для курсового проекту у CyberBionic Systematics
Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

from typing import Dict

import pygame

from players.player import Player
from players.dealer import Dealer
from sprites.desired_area import DesiredArea


class Game:
	FPS: int = 30
	WIDTH: int = 1357
	HEIGHT: int = 765

	def __init__(self, settings: Dict) -> None:
		"""Основний файл гри: логіка, гравці"""
		pygame.init()

		sc_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({settings.get("description")}) {settings.get("version_app")}')

		sc_table = pygame.image.load('images/blackjack-table.png').convert()
		sc_main.blit(sc_table, (0, 0))

		####################
		self.test = DesiredArea()
		sc_main.blit(self.test.get_current_sprite('worms', 'V'), (20, 100))
		sc_main.blit(self.test.get_current_sprite('peaks', '5'), (700, 100))
		sc_main.blit(self.test.get_current_sprite('peaks', '3'), (340, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '4'), (495, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '5'), (650, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '6'), (20, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '7'), (180, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '8'), (340, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '9'), (495, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', '10'), (650, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', 'V'), (20, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', 'D'), (180, 100))
		# sc_main.blit(self.test.get_current_sprite('peaks', 'K'), (340, 100))
		####################

		pygame.display.update()
		self.clock = pygame.time.Clock()

		self.player = Player()
		self.dealer = Dealer()

		self.main_game_loop()

	def main_game_loop(self) -> None:
		"""Основний цикл гри"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					pass

			self.clock.tick(self.FPS)
