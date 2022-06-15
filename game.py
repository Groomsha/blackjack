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

from typing import Dict, Any

import pygame

from players.player import Player
from players.dealer import Dealer

from creation.creation_chips import CreationChips
from creation.creation_cards import CreationCards
from creation.creation_shirts import CreationShirts
from sources.creation_deck import CreationDeck


class Game:
	FPS: int = 30
	WIDTH: int = 1357
	HEIGHT: int = 765

	def __init__(self, settings: Dict) -> None:
		"""Основний файл гри: логіка, гравці"""
		self.__settings = settings

		pygame.init()

		self.__sc_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({self.__settings.get("description")}) '
								   f'{self.__settings.get("version_app")}')

		sc_table = pygame.image.load('images/blackjack-table.png').convert()
		self.__sc_main.blit(sc_table, (0, 0))

		self.game_chips = GameCreationChips(self.__sc_main, self.__settings)

		self.deck = CreationDeck()	#колода
		self.deck.update_shuffled()

		self.creation_opponents()
		self.creation_object()
		self.main_game_loop()

	def creation_object(self):
		"""Метод створює об'єкти гри"""
		cards = CreationCards()
		card_sprite = cards.return_sprite_to_sc({'suit': 'worms', 'value': 'A', 'pos_c': (20, 500)})
		self.__sc_main.blit(card_sprite[0], card_sprite[1])
		card_sprite = cards.return_sprite_to_sc({'suit': 'peaks', 'value': '5', 'pos_c': (700, 500)})
		self.__sc_main.blit(card_sprite[0], card_sprite[1])
		card_sprite = cards.return_sprite_to_sc({'suit': 'peaks', 'value': '9', 'pos_c': (340, 500)})
		self.__sc_main.blit(card_sprite[0], card_sprite[1])

		shirts = CreationShirts()
		shirts_sprite = shirts.return_sprite_to_sc({'shirt': 'shirts', 'color': 'red', 'pos_c': (500, 500)})
		self.__sc_main.blit(shirts_sprite[0], shirts_sprite[1])
		shirts_sprite = shirts.return_sprite_to_sc({'shirt': 'shirts', 'color': 'blue', 'pos_c': (900, 500)})
		self.__sc_main.blit(shirts_sprite[0], shirts_sprite[1])

		pygame.display.update()

	def creation_opponents(self) -> None:
		"""Метод створює опонентів гри"""
		self.player = Player(self.__sc_main, self.__settings)
		self.dealer = Dealer(self.__sc_main, self.__settings)

	def main_game_loop(self) -> None:
		"""Основний цикл гри"""
		clock = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					pass

			clock.tick(self.FPS)


class GameCreationChips:
	def __init__(self, sc: Any, settings: Dict) -> None:
		__chips = CreationChips()
		__meaning_temp: Any = ''
		__counter: int = 0

		__chips_list: Dict = {'chip_1': {
								'pos_c': (975, 625), 'text': settings.get("chip_values")[0], 'pos_t': (975, 625)},
							'chip_2': {
								'pos_c': (1060, 625), 'text': settings.get("chip_values")[1], 'pos_t': (1060, 625)},
							'chip_3': {
								'pos_c': (1145, 625), 'text': settings.get("chip_values")[2], 'pos_t': (1145, 625)},
							'chip_4': {
								'pos_c': (1230, 625), 'text': settings.get("chip_values")[3], 'pos_t': (1230, 625)}
		}

		for meaning in __chips.return_sprite_to_sc(__chips_list):
			if __counter % 2 == 0:
				__meaning_temp = meaning
			else:
				sc.blit(__meaning_temp, meaning)
			__counter += 1
