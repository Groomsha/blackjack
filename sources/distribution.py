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

from typing import Tuple, Dict, Any

import pygame


class Distribution:
	def __init__(self, game: Any) -> None:
		self.main_game = game

	def create_sc_text(self, cursor: str, *args) -> None:
		sprite: pygame = None

		if cursor == 'player':
			sprite = self._creation_text((str(self.cash_current), 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (355, 738))

			sprite = self._creation_text((str(self.cash_total), 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (355, 738))
		elif cursor == 'dealer':
			temp_text: str = f'Dealer Score: {self.___dealer_score}'
			sprite = self._creation_text((str(temp_text), 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (590, 300))

			temp_text: str = f'Player Score: {self.___player_score}'
			sprite = self._creation_text((str(temp_text), 36, (255, 255, 255)))
			self.main_game.sc_main.blit(sprite, (590, 570))
		elif cursor == 'win':
			pass

	@staticmethod
	def _creation_text(options: Tuple[str, int, Tuple[int, int, int]]) -> pygame.Surface:
		"""Створення тексту гравців"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
