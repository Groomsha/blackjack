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

from typing import Dict, Tuple, List, Any

from players.base import Base
from sources.creation_deck import CreationDeck
from creation.creation_cards import CreationCards
from creation.creation_shirts import CreationShirts


class Dealer(Base):
	def __init__(self, sc: Any) -> None:
		"""Клас для логіки дилера"""
		super(Dealer, self).__init__(sc)

		self.__deck = CreationDeck()
		self.__deck.update_shuffled()

		self.__player_cards: Tuple = tuple()
		self.__dealer_cards: Tuple = tuple()

		# self.distribution()

	def distribution(self) -> None:
		cards = CreationCards()
		shirts = CreationShirts()

		self.__dealer_cards += self.__deck.shuffled_deck[0]
		self.__dealer_cards += self.__deck.shuffled_deck[1]

		self.__player_cards += self.__deck.shuffled_deck[2]
		self.__player_cards += self.__deck.shuffled_deck[3]

		card_sprite = cards.return_sprite_to_sc({'suit': self.__dealer_cards[0], 'value': self.__dealer_cards[1], 'pos_c': (600, 200)})
		self.logic.main_game.sc_main.blit(card_sprite[0], card_sprite[1])
		shirts_sprite = shirts.return_sprite_to_sc({'shirt': 'shirts', 'color': self.logic.main_game.shirts_color, 'pos_c': (680, 200)})
		self.logic.main_game.sc_main.blit(shirts_sprite[0], shirts_sprite[1])

		card_sprite = cards.return_sprite_to_sc({'suit': self.__player_cards[0], 'value': self.__player_cards[1], 'pos_c': (600, 470)})
		self.logic.main_game.sc_main.blit(card_sprite[0], card_sprite[1])
		card_sprite = cards.return_sprite_to_sc({'suit': self.__player_cards[2], 'value': self.__player_cards[3], 'pos_c': (680, 470)})
		self.logic.main_game.sc_main.blit(card_sprite[0], card_sprite[1])

		self.dealer_score = self.__count_score_distribution(self.__dealer_cards[1])
		self.player_score = self.__count_score_distribution(self.__player_cards[1], self.__player_cards[3])
		self.logic.create_sc_text('dealer', f'Dealer Score: {self.dealer_score}', f'Player Score: {self.player_score}')

	def player_game(self):
		pass

	def dealer_game(self):
		self.logic.main_game.creation_object()

	@staticmethod
	def __count_score_distribution(*args) -> int:
		temp_list: List = []

		for literal in args:
			if not literal in 'AVDK':
				temp_list.append(int(literal))
			elif literal in 'VDK':
				temp_list.append(10)
			elif literal == 'A':
				temp_list.append(11)

		return sum(temp_list)
