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

from creation.creation_chips import CreationChips


class Game:
	FPS: int = 30
	WIDTH: int = 1357
	HEIGHT: int = 765

	def __init__(self, settings: Dict[str, str]) -> None:
		"""Основний файл гри: логіка, гравці"""
		self.__settings: Dict[str, str] = settings
		self.__game_chips: GameCreationChips = None
		self.__sc_main: pygame = None
		self.__player: Player = None
		self.__dealer: Dealer = None

		pygame.init()

		self.__sc_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({self.__settings.get("description")}) '
								f''f'{self.__settings.get("version_app")}')

		self.__creation_object()
		self.__creation_opponents()

		pygame.display.update()
		self.__main_game_loop()

	def __creation_object(self) -> None:
		"""Метод створює об'єкти на ігровому полі"""
		sc_table: pygame.Surface = pygame.image.load('images/blackjack-table.png').convert()
		self.__sc_main.blit(sc_table, (0, 0))

		self.__game_chips = GameCreationChips(self.__sc_main, self.__settings)

	def __creation_opponents(self) -> None:
		"""Метод створює опонентів гри"""
		self.__player = Player(self.__sc_main, self.__settings)
		self.__dealer = Dealer(self.__sc_main, self.__settings)

	def __main_game_loop(self) -> None:
		"""Основний цикл гри"""
		clock: pygame = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					x, y = pygame.mouse.get_pos()

					if not self.__player.start_game:
						chip = self.__game_chips._mouse_event_click(x, y)
						print(chip)

			clock.tick(self.FPS)


class GameCreationChips:
	def __init__(self, sc: pygame, settings: Dict) -> None:
		"""Клас створює та відображає фішки на ігровому полі"""
		__meaning_temp: pygame.Surface = None
		__chips = CreationChips()
		__counter: int = 0

		__chips_dict: Dict = {'chip_1': {
								'pos_c': (975, 625), 'text': settings.get("chip_values")[0], 'pos_t': (1010, 675)},
							'chip_2': {
								'pos_c': (1060, 625), 'text': settings.get("chip_values")[1], 'pos_t': (1090, 675)},
							'chip_3': {
								'pos_c': (1145, 625), 'text': settings.get("chip_values")[2], 'pos_t': (1175, 675)},
							'chip_4': {
								'pos_c': (1230, 625), 'text': settings.get("chip_values")[3], 'pos_t': (1255, 675)}
		}

		for meaning in __chips.return_sprite_to_sc(__chips_dict):
			if __counter % 2 == 0:
				__meaning_temp = meaning
			else:
				sc.blit(__meaning_temp, meaning)
			__counter += 1

	@staticmethod
	def _mouse_event_click(mouse_x: int, mouse_y: int) -> int:
		if 975 <= mouse_x <= 1055 and 655 <= mouse_y <= 725:
			return -1
		elif 1065 <= mouse_x <= 1145 and 655 <= mouse_y <= 725:
			return 25
		elif 1155 <= mouse_x <= 1235 and 655 <= mouse_y <= 725:
			return 50
		elif 1245 <= mouse_x <= 1560 and 655 <= mouse_y <= 725:
			return 100
