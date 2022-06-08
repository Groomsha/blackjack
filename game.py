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

from players.player import Player
from players.dealer import Dealer


class Game:
	FPS: int = 30
	WIDTH: int = 800
	HEIGHT: int = 600

	def __init__(self, settings: Dict) -> None:
		"""Основний файл гри: логіка, гравці"""
		pygame.init()
		self.clock = pygame.time.Clock()

		pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({settings.get("description")}) {settings.get("version_app")}')

		self.player = Player()
		self.dealer = Dealer()

		self.main_game_loop()

	def main_game_loop(self) -> None:
		"""Основний цикл гри"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

			self.clock.tick(self.FPS)
