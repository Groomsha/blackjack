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
	def __init__(self, sprite_map: List) -> None:
		"""Клас вирізає певну область на зображенні, і повертається із зазначеними параметрами в json """
		self.__sprite_sheet = pygame.image.load(sprite_map[0]).convert()

		with open(sprite_map[1]) as file:
			self.__sprite_map = load(file)

	def __get_sprite(self, setings: List) -> Any:
		"""Метод повертає вирізану область із зазначеними параметрами"""
		sprite = pygame.Surface((setings[2], setings[3]))

		if setings[8]:
			sprite.set_colorkey((0, 0, 0))

		sprite.blit(self.__sprite_sheet, (0, 0), (setings[0], setings[1], setings[2], setings[3]))
		sprite = pygame.transform.scale(sprite, (setings[4], setings[5]))
		sprite = pygame.transform.rotate(sprite, setings[6])

		return sprite

	def parse_sprite(self, name) -> Any:
		"""Метод повертає іменовану область"""
		setings_sprite: List = []

		sprite = self.__sprite_map['frames'][name]['frame']
		setings_sprite.extend([sprite["x"], sprite["y"], sprite["w"], sprite["h"]])

		sprite = self.__sprite_map['frames'][name]['frameSize']
		setings_sprite.extend([sprite["w"], sprite["h"]])

		sprite = self.__sprite_map['frames'][name]['rotated']
		setings_sprite.extend([sprite["x"], sprite["y"]])

		setings_sprite.append(self.__sprite_map['frames'][name]['alfa24'])

		image = self.__get_sprite(setings_sprite)

		return image
