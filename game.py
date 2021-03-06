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

import random
from typing import Dict

import pygame

from players.player import Player
from players.dealer import Dealer
from sources.distribution import Distribution

from creation.creation_chips import CreationChips
from creation.creation_shirts import CreationShirts


class Game:
	FPS: int = 30
	WIDTH: int = 1357
	HEIGHT: int = 765

	def __init__(self, settings: Dict[str, str]) -> None:
		"""Основний файл гри: логіка, гравці"""
		self.__settings: Dict[str, str] = settings
		self.__game_chips: GameCreationChips = None
		self.__logic: Distribution = Distribution(self)
		self.__sc_main: pygame = None
		self.__player: Player = None
		self.__dealer: Dealer = None

		pygame.init()

		self.__shirts_color: str = 'red' if random.randint(0, 1) else 'blue'
		self.__sc_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({self.__settings.get("description")}) {self.__settings.get("version_app")}')

		self.creation_object()
		self.__creation_opponents()
		self.__main_game_loop()

	@property
	def sc_main(self) ->pygame:
		return self.__sc_main

	@property
	def logic(self) -> Distribution:
		return self.__logic

	@property
	def settings(self) -> Dict:
		return self.__settings

	@property
	def shirts_color(self) -> str:
		return self.__shirts_color

	def creation_object(self) -> None:
		"""Метод створює об'єкти на ігровому полі"""
		shirts = CreationShirts()
		shirts_sprite = shirts.return_sprite_to_sc(
			{'shirt': 'shirts', 'color': self.__shirts_color, 'pos_c': (917, 150)})

		sc_table: pygame.Surface = pygame.image.load('images/blackjack-table.png').convert()
		sc_shirts = pygame.transform.rotate(shirts_sprite[0].convert_alpha(), 65)

		self.__sc_main.blit(sc_table, (0, 0))
		self.__sc_main.blit(sc_shirts, shirts_sprite[1])

		self.__game_chips = GameCreationChips(self.__sc_main, self.__settings)

	def __creation_opponents(self) -> None:
		"""Метод створює опонентів гри"""
		self.__player = Player(self)
		self.__dealer = Dealer(self)

	def __main_game_loop(self) -> None:
		"""Основний цикл гри"""
		clock: pygame = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					x, y = pygame.mouse.get_pos()

					if not self.__logic.start_game:
						chip_val: int = self.__game_chips.mouse_event_click(x, y)

						if not chip_val == None:
							self.__player.current_rate(chip_val)
						else:
							if self.logic.cash_current > 0:
								self.__player.mouse_event_click_bit(x, y)

								if self.__logic.start_game:
									self.__dealer.start_distribution('start')
					else:
						self.__player.mouse_event_click_game(x, y)

						if self.__logic.player_pass:
							self.__logic.player_pass = False
							self.__dealer.dealer_game(True)

						if self.__logic.player_add:
							self.__logic.player_add = False
							self.__dealer.player_game()

			clock.tick(self.FPS)
			pygame.display.update()


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
	def mouse_event_click(mouse_x: int, mouse_y: int) -> int:
		if 975 <= mouse_x <= 1055 and 655 <= mouse_y <= 725:
			return -1
		elif 1065 <= mouse_x <= 1145 and 655 <= mouse_y <= 725:
			return 25
		elif 1155 <= mouse_x <= 1235 and 655 <= mouse_y <= 725:
			return 50
		elif 1245 <= mouse_x <= 1560 and 655 <= mouse_y <= 725:
			return 100
