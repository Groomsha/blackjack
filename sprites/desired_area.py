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

from typing import Dict, List

import pygame

from sprites.spritesheet import SpriteSheet


class DesiredArea:
	def __init__(self) -> None:
		"""Клас вибирає потрібну область на зображенні"""
		self.__cards_dict: Dict[str, List[str]] = {
			'clubs': ['images/blackjack-cards.png', 'json_imag/cards_clubs.json'],
			'timbrel': ['images/blackjack-cards.png', 'json_imag/cards_timbrel.json'],
			'worms': ['images/blackjack-cards.png', 'json_imag/cards_worms.json'],
			'peaks': ['images/blackjack-cards.png', 'json_imag/cards_peaks.json'],
			'shirts': ['images/blackjack-shirt.png', 'json_imag/cards_shirts.json'],
			'chips': ['images/blackjack-chips.png', 'json_imag/cards_chips.json'],
			'button': ['images/blackjack-button.png', 'json_imag/cards_button.json'],
		}

	@property
	def cards_dict(self) -> Dict[str, List[str]]:
		"""Get повертає Dict з посиланнями на ігрові об'єкти (images, json)"""
		return self.__cards_dict

	def get_current_sprite(self, name: str, denomination: str) -> pygame.surface:
		"""Створює об'єкт SpriteSheet із потрібної області"""
		current_card = SpriteSheet(self.cards_dict.get(name))

		return current_card.parse_sprite(f'{name}_{denomination}.png')
