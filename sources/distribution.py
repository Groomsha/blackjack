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

from typing import Tuple, Any

import pygame

from creation.creation_cards import CreationCards
from creation.creation_shirts import CreationShirts
from creation.creation_button import CreationButton


class Distribution:
	def __init__(self, game: Any) -> None:
		self.main_game = game

		self.start_game: bool = False
		self.player_add: bool = False
		self.player_pass: bool = False

		self.player_score: int = 0
		self.dealer_score: int = 0

		self.cash_current: int = 0
		self.cash_total: int = int(game.settings['game_amount'])

	def create_sc_text(self, cursor: str, *args) -> None:
		if cursor == 'player':
			sprite = self.__creation_text((args[0], 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (355, 738))

			sprite = self.__creation_text((args[1], 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (1065, 738))
		elif cursor == 'dealer':
			sprite = self.__creation_text((args[0], 36, (0, 0, 0)))
			self.main_game.sc_main.blit(sprite, (590, 300))

			sprite = self.__creation_text((args[1], 36, (0, 0, 0)))
			self.main_game.sc_main.blit(sprite, (590, 570))
		elif cursor == 'win':
			sprite = self.__creation_text((args[0], 44, (0, 0, 0)))
			self.main_game.sc_main.blit(sprite, (600, 390))

	def create_sc_buttons(self, cursor: str) -> None:
		button = CreationButton()

		if cursor == 'bit':
			sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'deal', 'pos_c': (630, 630)})
			self.main_game.sc_main.blit(sprite[0], sprite[1])
		elif cursor == 'game':
			sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'yes', 'pos_c': (580, 630)})
			self.main_game.sc_main.blit(sprite[0], sprite[1])

			sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'no', 'pos_c': (680, 630)})
			self.main_game.sc_main.blit(sprite[0], sprite[1])

	def buttons_sc_cards(self, cursor: str, dealer: Tuple, player: Tuple):
		color_opt: str = self.main_game.shirts_color
		pos_player_x: int = 600
		pos_dealer_x: int = 600
		pos_step: int = 80
		counter: int = 0

		cards = CreationCards()
		shirts = CreationShirts()

		if cursor == 'start' or cursor == 'player':
			sprite = cards.return_sprite_to_sc({'suit': dealer[0], 'value': dealer[1], 'pos_c': (600, 200)})
			self.main_game.sc_main.blit(sprite[0], sprite[1])

			sprite = shirts.return_sprite_to_sc({'shirt': 'shirts', 'color': color_opt, 'pos_c': (680, 200)})
			self.main_game.sc_main.blit(sprite[0], sprite[1])

			for _ in player:
				if not counter%2 == 0:
					if counter > 1:
						pos_player_x += pos_step

					sprite = cards.return_sprite_to_sc({'suit': player[counter-1], 'value': player[counter], 'pos_c': (pos_player_x, 470)})
					self.main_game.sc_main.blit(sprite[0], sprite[1])
				counter += 1

		elif cursor == 'dealer':
			for _ in dealer:
				if not counter%2 == 0:
					if counter > 1:
						pos_dealer_x += pos_step

					sprite = cards.return_sprite_to_sc({'suit': dealer[counter-1], 'value': dealer[counter], 'pos_c': (pos_dealer_x, 200)})
					self.main_game.sc_main.blit(sprite[0], sprite[1])
				counter += 1

			counter = 0

			for _ in player:
				if not counter%2 == 0:
					if counter > 1:
						pos_player_x += pos_step

					sprite = cards.return_sprite_to_sc({'suit': player[counter-1], 'value': player[counter], 'pos_c': (pos_player_x, 470)})
					self.main_game.sc_main.blit(sprite[0], sprite[1])
				counter += 1

	@staticmethod
	def __creation_text(options: Tuple[str, int, Tuple[int, int, int]]) -> pygame.Surface:
		"""Створення тексту гравців"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
