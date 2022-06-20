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

from players.base import Base
from sources.creation_deck import CreationDeck
from creation.creation_cards import CreationCards


class Dealer(Base):
	def __init__(self, sc: pygame, settings: Dict[str, str]) -> None:
		"""Клас для логіки дилера"""
		super(Dealer, self).__init__(sc, settings)

		self.deck = CreationDeck()
		self.deck.update_shuffled()

		self._creation_object()

	def _creation_object(self) -> None:
		"""Метод створює об'єкти гри"""
		super(Dealer, self)._creation_object()

		cards = CreationCards()
		card_sprite = cards.return_sprite_to_sc({'suit': 'worms', 'value': 'A', 'pos_c': (20, 500)})
		self.sc_main.blit(card_sprite[0], card_sprite[1])
		card_sprite = cards.return_sprite_to_sc({'suit': 'peaks', 'value': '5', 'pos_c': (700, 500)})
		self.sc_main.blit(card_sprite[0], card_sprite[1])
		card_sprite = cards.return_sprite_to_sc({'suit': 'peaks', 'value': '9', 'pos_c': (340, 500)})
		self.sc_main.blit(card_sprite[0], card_sprite[1])
