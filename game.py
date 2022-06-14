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

from players.player import Player
from players.dealer import Dealer

from sprites.desired_area import DesiredArea
from creation.creation_chips import CreationChips


class Game:
	FPS: int = 30
	WIDTH: int = 1357
	HEIGHT: int = 765

	def __init__(self, settings: Dict) -> None:
		"""Основний файл гри: логіка, гравці"""
		self.__settings = settings

		pygame.init()

		self.__sc_main = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_icon(pygame.image.load('images/blackjack-icon.ico'))
		pygame.display.set_caption(f'BlackJack ({self.settings.get("description")}) {self.settings.get("version_app")}')

		self.creation_opponents()
		self.creation_object()
		self.main_game_loop()

	@property
	def settings(self) -> Dict:
		"""Get повертає об'єкт ігрового поля"""
		return self.__settings

	@property
	def sc_main(self) -> Any:
		"""Get повертає об'єкт ігрового поля"""
		return self.__sc_main

	def creation_object(self):
		"""Метод створює об'єкти гри"""
		sc_table = pygame.image.load('images/blackjack-table.png').convert()
		self.sc_main.blit(sc_table, (0, 0))

		chips = CreationChips(self.sc_main)
		chips_list: Dict = {'chip_1': {
								'pos_c': (975, 625), 'text': self.settings.get("chip_values")[0], 'pos_t': (975, 625)},
							'chip_2': {
								'pos_c': (1060, 625), 'text': self.settings.get("chip_values")[1], 'pos_t': (1060, 625)},
							'chip_3': {
								'pos_c': (1145, 625), 'text': self.settings.get("chip_values")[2], 'pos_t': (1145, 625)},
							'chip_4': {
								'pos_c': (1230, 625), 'text': self.settings.get("chip_values")[3], 'pos_t': (1230, 625)}
							}

		chips._creation_sprite_to_sc(chips_list)

		##########TEST##########
		test = DesiredArea()

		self.sc_main.blit(test.get_current_sprite('worms', 'V'), (20, 500))
		self.sc_main.blit(test.get_current_sprite('peaks', '5'), (700, 500))
		self.sc_main.blit(test.get_current_sprite('peaks', '3'), (340, 500))
		########################

		pygame.display.update()

	def creation_opponents(self) -> None:
		"""Метод створює опонентів гри"""
		self.player = Player()
		self.dealer = Dealer()

	def main_game_loop(self) -> None:
		"""Основний цикл гри"""
		clock = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					pass

			clock.tick(self.FPS)
