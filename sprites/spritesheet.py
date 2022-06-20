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

from json import load
from typing import List, Any

import pygame


class SpriteSheet:
	def __init__(self, sprite_map: List[str]) -> None:
		"""Клас вирізає певну область на зображенні, і повертається із зазначеними параметрами в json """
		self.__sprite_sheet = pygame.image.load(sprite_map[0]).convert()

		with open(sprite_map[1]) as file:
			self.__sprite_map = load(file)

	def __get_sprite(self, settings: List[Any]) -> pygame.Surface:
		"""Метод повертає вирізану область із зазначеними параметрами"""
		sprite = pygame.Surface((settings[2], settings[3]))

		if settings[8]:
			sprite.set_colorkey((0, 0, 0))

		sprite.blit(self.__sprite_sheet, (0, 0), (settings[0], settings[1], settings[2], settings[3]))
		sprite = pygame.transform.scale(sprite, (settings[4], settings[5]))
		sprite = pygame.transform.rotate(sprite, settings[6])

		return sprite

	def parse_sprite(self, name: str) -> pygame.Surface:
		"""Метод повертає іменовану область"""
		settings_sprite: List[Any] = []

		sprite = self.__sprite_map['frames'][name]['frame']
		settings_sprite.extend([sprite["x"], sprite["y"], sprite["w"], sprite["h"]])

		sprite = self.__sprite_map['frames'][name]['frameSize']
		settings_sprite.extend([sprite["w"], sprite["h"]])

		sprite = self.__sprite_map['frames'][name]['rotated']
		settings_sprite.extend([sprite["x"], sprite["y"]])

		settings_sprite.append(self.__sprite_map['frames'][name]['alfa24'])

		image = self.__get_sprite(settings_sprite)

		return image
