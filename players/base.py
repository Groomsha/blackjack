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

from typing import Dict, Tuple, Any

import pygame

from sources.distribution import Distribution


class Base:
	def __init__(self, sc: Any, settings: Dict[str, str]) -> None:
		"""Базовий клас для логіки гравців"""
		self.__sc_main: pygame = sc.sc_main
		self.__start_game: bool = False
		self.__settings: Dict[str, str] = settings
		self.__logic: Any = Distribution(sc)

		self.cash_current_: int = 0
		self.cash_total: int = int(self.settings['game_amount'])

	@property
	def settings(self) -> Dict[str, str]:
		"""Get повертає налаштування ігрового поля"""
		return self.__settings

	@property
	def sc_main(self) -> pygame:
		"""Get повертає об'єкт ігрового поля"""
		return self.__sc_main

	@property
	def logic(self) -> Distribution:
		"""Get повертає об'єкт ігрового поля"""
		return self.__logic

	@property
	def start_game(self) -> bool:
		return self.__start_game

	@start_game.setter
	def start_game(self, val: bool) -> None:
		self.__start_game = val

	def _creation_object(self) -> None:
		"""Метод створює об'єкти гри"""
		pass

	@staticmethod
	def _creation_text(options: Tuple[str, int, Tuple[int, int, int]]) -> pygame.Surface:
		"""Створення тексту гравців"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
