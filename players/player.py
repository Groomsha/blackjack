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

from players.base import Base
from creation.creation_button import CreationButton


class Player(Base):
	def __init__(self, sc: pygame, settings: Dict[str, str]) -> None:
		"""Клас для логіки гравця"""
		super(Player, self).__init__(sc, settings)

		self.game_class = sc
		self.__cash_current: int = 0
		self.__cash_total: int = int(self.settings['game_amount'])

		self.create_sc_text()
		self.button_bit()

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
		self.create_sc_text()
		self.button_bit()

	def button_bit(self) -> None:
		button = CreationButton()
		bit_sprite = button.return_sprite_to_sc({'suit': 'button', 'value': 'deal', 'pos_c': (630, 630)})
		self.sc_main.blit(bit_sprite[0], bit_sprite[1])

	def create_sc_text(self) -> None:
		self.__cash: pygame.Surface = self._creation_text((str(self.__cash_current), 36, (255, 255, 255)))
		self.__total: pygame.Surface = self._creation_text((str(self.__cash_total), 36, (255, 255, 255)))

		self.sc_main.blit(self.__cash, (355, 738))
		self.sc_main.blit(self.__total, (1065, 738))
