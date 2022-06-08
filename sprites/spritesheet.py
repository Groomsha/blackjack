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
from typing import List

import pygame


class SpriteSheet:
	def __init__(self, sprite_map: List) -> None:
		"""Клас вирізає певну область на зображенні"""
		self.__sprite_sheet = pygame.image.load(sprite_map[0]).convert()

		with open(sprite_map[1]) as file:
			self.__sprite_map = load(file)

	@property
	def sprite_sheet(self):
		return self.__sprite_sheet

	@property
	def sprite_map(self):
		return self.__sprite_map

	def __get_sprite(self, x, y, w, h):
		"""Метод повертає вирізану область"""
		sprite = pygame.Surface((w, h))
		sprite.set_colorkey((0, 0, 0))
		sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))

		return sprite

	def parse_sprite(self, name):
		"""Метод повертає іменовану область"""
		sprite = self.sprite_map['frames'][name]['frame']
		x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
		image = self.__get_sprite(x, y, w, h)

		return image
