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

from typing import Any, Tuple, Dict

import pygame

from sprites.desired_area import DesiredArea


class CreationBase:
	"""Базовий клас для виведення ігрових об'єктів"""
	def __init__(self) -> None:
		self._sprite_tuple: Tuple = ()

		self._sc_text = CreationText()
		self._sprite_area = DesiredArea()

	def _creation_sprite_to_sc(self, quantity: Dict[str, Any]) -> Tuple[pygame.Surface, Tuple[int, int]]:
		"""Створення ігрового об'єкту на полі"""
		pass

	def return_sprite_to_sc(self, quantity: Dict[str, Any]) -> Tuple[pygame.Surface, Tuple[int, int]]:
		"""Повертає ігровий об'єкт на поле"""
		pass


class CreationText:
	"""Базовий клас для виведення тексту до ігрових об'єктів"""
	def __init__(self) -> None:
		pass

	def _creation_text_to_sc(self, options: Tuple[str, int, Tuple[int, int, int]]) -> pygame.Surface:
		"""Створення тексту для ігрового об'єкту на полі"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
