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
import time
from typing import List, Tuple, Any

from sources.creation_deck import CreationDeck


class Dealer:
	def __init__(self, sc: Any) -> None:
		"""Клас для логіки дилера"""
		self.main_game = sc

		self.__deck = CreationDeck()
		self.__deck.update_shuffled()

		self.__dealer_cards: Tuple = self.__deck.shuffled_deck[0]
		self.__dealer_cards += self.__deck.shuffled_deck[1]

		self.__player_cards: Tuple = self.__deck.shuffled_deck[2]
		self.__player_cards += self.__deck.shuffled_deck[3]

	def start_distribution(self) -> None:
		self.main_game.logic.buttons_sc_cards('start', self.__dealer_cards, self.__player_cards)

		self.main_game.logic.dealer_score = self.__count_score_distribution(self.__dealer_cards[1])
		self.main_game.logic.player_score = self.__count_score_distribution(self.__player_cards[1], self.__player_cards[3])

		self.main_game.logic.create_sc_text('dealer', f'Dealer Score: {self.main_game.logic.dealer_score}', f'Player Score: {self.main_game.logic.player_score}')

	def player_game(self):
		pass

	def dealer_game(self):
		self.main_game.logic.create_sc_text('win', self.__game_win_distribution(self.main_game.logic.dealer_score, self.main_game.logic.player_score))

		self.main_game.creation_object()
		self.main_game.logic.start_game = False
		self.main_game.logic.player_add = False
		self.main_game.logic.player_pass = False
		self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current), str(self.main_game.logic.cash_total))
		self.main_game.logic.create_sc_buttons('start')


	def __game_win_distribution(self, *args) -> str:
		if args[0] > args[1] <= 21:
			self.main_game.logic.cash_total -= self.main_game.logic.cash_current
			self.main_game.logic.cash_current = 0
			return 'Dealer WIN!'
		elif args[1] > args[0] <= 21:
			self.main_game.logic.cash_total += self.main_game.logic.cash_current
			self.main_game.logic.cash_current = 0
			return 'Player WIN!'

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
