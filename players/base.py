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
from typing import Dict, Tuple

import pygame

from creation.creation_shirts import CreationShirts


class Base:
	def __init__(self, sc: pygame, settings: Dict[str, str]) -> None:
		"""Базовий клас для логіки гравців"""
		self.__sc_main: pygame = sc
		self.__settings: Dict[str, str] = settings
		self.__cash: pygame.Surface = self._creation_text(('0', 36, (255, 255, 255)))
		self.__total: pygame.Surface = self._creation_text((self.__settings['game_amount'], 36, (255, 255, 255)))

		self.__sc_main.blit(self.__cash, (355, 738))
		self.__sc_main.blit(self.__total, (1065, 738))

		self._shirts_color: str = 'red' if random.randint(0, 1) else 'blue'

	@property
	def settings(self) -> Dict[str, str]:
		"""Get повертає налаштування ігрового поля"""
		return self.__settings

	@property
	def sc_main(self) -> pygame:
		"""Get повертає об'єкт ігрового поля"""
		return self.__sc_main

	def _creation_object(self) -> None:
		"""Метод створює об'єкти гри"""
		shirts = CreationShirts()

		shirts_sprite = shirts.return_sprite_to_sc({'shirt': 'shirts', 'color': self._shirts_color, 'pos_c': (917, 150)})
		shirts_rotate = pygame.transform.rotate(shirts_sprite[0].convert_alpha(), 65)
		self.sc_main.blit(shirts_rotate, shirts_sprite[1])

	@staticmethod
	def _creation_text(options: Tuple[str, int, Tuple[int, int, int]]) -> pygame.Surface:
		"""Створення тексту гравців"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
