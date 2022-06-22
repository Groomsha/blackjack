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

from players.base import Base
from creation.creation_button import CreationButton


class Player(Base):
	def __init__(self, sc: Any, settings: Dict[str, str]) -> None:
		"""Клас для логіки гравця"""
		super(Player, self).__init__(sc, settings)

		self.game_class = sc
		self.__cash_current: int = 0
		self.__cash_total: int = int(self.settings['game_amount'])

		self.__create_sc_text()
		self.__button_bit()

	@property
	def cash_current(self) -> int:
		return self.__cash_current

	def current_rate(self, chip_val: int) -> None:
		if not chip_val == -1:
			temp = self.__cash_total - chip_val

			if temp >= 0:
				self.__cash_total -= chip_val
				self.__cash_current += chip_val
		else:
			self.__cash_total += self.__cash_current
			self.__cash_current = 0

		self.game_class.creation_object()
		self.__create_sc_text()
		self.__button_bit()

	def __button_bit(self) -> None:
		button = CreationButton()
		bit_sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'deal', 'pos_c': (630, 630)})
		self.sc_main.blit(bit_sprite[0], bit_sprite[1])

	def __button_game(self) -> None:
		button = CreationButton()

		yes_sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'yes', 'pos_c': (580, 630)})
		no_sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'no', 'pos_c': (680, 630)})

		self.sc_main.blit(yes_sprite[0], yes_sprite[1])
		self.sc_main.blit(no_sprite[0], no_sprite[1])

	def __create_sc_text(self) -> None:
		self.__cash: pygame.Surface = self._creation_text((str(self.__cash_current), 36, (255, 255, 255)))
		self.__total: pygame.Surface = self._creation_text((str(self.__cash_total), 36, (255, 255, 255)))

		self.sc_main.blit(self.__cash, (355, 738))
		self.sc_main.blit(self.__total, (1065, 738))

	def mouse_event_click_bit(self, mouse_x: int, mouse_y: int) -> None:
		if 635 <= mouse_x <= 715 and 635 <= mouse_y <= 715:
			self.start_game = True
			self.game_class.creation_object()
			self.__create_sc_text()
			self.__button_game()
			print('Start Game')

	def mouse_event_click_game(self, mouse_x: int, mouse_y: int) -> None:
		if 585 <= mouse_x <= 665 and 635 <= mouse_y <= 715:
			print('Add Card')
		elif 685 <= mouse_x <= 765 and 635 <= mouse_y <= 715:
			print('Pass')
