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
from threading import Timer
from typing import List, Tuple, Any

from sources.creation_deck import CreationDeck


class Dealer:
	def __init__(self, sc: Any) -> None:
		"""Клас для логіки дилера"""
		self.main_game = sc

		self.__deck_new = CreationDeck()
		self.__deck_new.update_shuffled()

		self.__deck_shuffled = [deck for deck in self.__deck_new.shuffled_deck]

		self.__dealer_cards: Tuple = None
		self.__player_cards: Tuple = None

	def start_distribution(self, cursor: str) -> None:
		if cursor == 'start':
			self.__dealer_cards = self.__deck_shuffled.pop(0)
			self.__dealer_cards += self.__deck_shuffled.pop(0)

			self.__player_cards = self.__deck_shuffled.pop(0)
			self.__player_cards += self.__deck_shuffled.pop(0)

			self.main_game.logic.buttons_sc_cards('start', self.__dealer_cards, self.__player_cards)
			self.main_game.logic.dealer_score = self.__count_score_distribution(self.__dealer_cards[1])
		elif cursor == 'player':
			self.__player_cards += self.__deck_shuffled.pop(0)

			self.main_game.logic.buttons_sc_cards('player', self.__dealer_cards, self.__player_cards)
			self.main_game.logic.dealer_score = self.__count_score_distribution(self.__dealer_cards[1])
		elif cursor == 'dealer':

			counter: int = 0
			count_score: List = []
			while True:
				for number in self.__dealer_cards:
					if not counter % 2 == 0:
						count_score.append(number)
					counter += 1

				if self.__count_score_distribution(count_score) <= 19:
					self.__dealer_cards += self.__deck_shuffled.pop(0)
				else:
					self.main_game.logic.buttons_sc_cards('dealer', self.__dealer_cards, self.__player_cards)
					break

			counter: int = 0
			count_score: List = []
			for number in self.__dealer_cards:
				if not counter % 2 == 0:
					count_score.append(number)
				counter += 1

			self.main_game.logic.dealer_score = self.__count_score_distribution(count_score)

		counter: int = 0
		count_score: List = []
		for number in self.__player_cards:
			if not counter % 2 == 0:
				count_score.append(number)
			counter += 1

		self.main_game.logic.player_score = self.__count_score_distribution(count_score)
		self.main_game.logic.create_sc_text('dealer', f'Dealer Score: {self.main_game.logic.dealer_score}', f'Player Score: {self.main_game.logic.player_score}')

	def player_game(self):
		self.main_game.creation_object()
		self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current), str(self.main_game.logic.cash_total))
		self.main_game.logic.create_sc_buttons('game')
		self.start_distribution('player')

	def dealer_game(self, cursor: bool):
		if cursor:
			self.main_game.creation_object()
			self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current),str(self.main_game.logic.cash_total))
			self.start_distribution('dealer')

		#####################################################
		self.main_game.logic.create_sc_text('win', self.__game_win_distribution(self.main_game.logic.dealer_score, self.main_game.logic.player_score))
		self.__dealer_cards = None
		self.__player_cards = None

		timer_to_new_game = Timer(2, self.new_game)
		timer_to_new_game.start()

	def new_game(self) -> None:
		self.main_game.creation_object()
		self.main_game.logic.start_game = False
		self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current),str(self.main_game.logic.cash_total))
		self.main_game.logic.create_sc_buttons('start')

	def __game_win_distribution(self, *args) -> str:
		if args[0] <= 21:
			if args[0] > args[1]:
				return 'Dealer WIN!'
		else:
			pass

		if args[1] <= 21:
			if args[1] > args[0]:
				return 'Player WIN!'
		else:
			pass

		# if args[0] <= 21 or args[1] <= 21:
		# 	print('One')
		# 	if args[1] > args[0]:
		# 		if args[1] <= 21:
		# 			self.main_game.logic.cash_total += self.main_game.logic.cash_current * 2
		# 			self.main_game.logic.cash_current = 0
		# 			return 'Player WIN!'
		# 	elif args[0] > args[1]:
		# 		if args[0] <= 21:
		# 			self.main_game.logic.cash_current = 0
		# 			return 'Dealer WIN!'
		# 	elif args[0] < args[1]:
		# 		if args[1] > 21:
		# 			self.main_game.logic.cash_current = 0
		# 			return 'Dealer WIN!'
		# 	elif args[0] == args[1]:
		# 		self.main_game.logic.cash_total += self.main_game.logic.cash_current
		# 		self.main_game.logic.cash_current = 0
		# 		return 'Draw!'
		# else:
		# 	print('Two')
		# 	self.main_game.logic.cash_total += self.main_game.logic.cash_current
		# 	self.main_game.logic.cash_current = 0
		# 	return 'Draw!'

		# if args[0] > 21 and args[1] > 21:
		# 	self.main_game.logic.cash_total += self.main_game.logic.cash_current
		# 	self.main_game.logic.cash_current = 0
		# 	return 'Draw!'
			# if args[0] > 21:
			# 	self.main_game.logic.cash_total += self.main_game.logic.cash_current * 2
			# 	self.main_game.logic.cash_current = 0
			# 	return 'Player WIN!'
			# elif args[1] > 21:
			# 	self.main_game.logic.cash_current = 0
			# 	return 'Dealer WIN!'

	@staticmethod
	def __count_score_distribution(*args) -> int:
		temp_list: List = []
		ace = False

		for literal in args[0]:
			if not literal in 'AVDK':
				temp_list.append(int(literal))
			elif literal in 'VDK':
				temp_list.append(10)
			elif literal == 'A':
				ace = True
				temp_list.append(11)
			elif literal == 'A' and ace:
				temp_list.append(1)

		return sum(temp_list)
