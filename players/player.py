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

from typing import Any


class Player:
	def __init__(self, sc: Any) -> None:
		"""Клас для логіки гравця"""
		self.main_game = sc

		self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current), str(self.main_game.logic.cash_total))

	def current_rate(self, chip_val: int) -> None:
		if not chip_val == -1:
			temp = self.main_game.logic.cash_total - chip_val

			if temp >= 0:
				self.main_game.logic.cash_total -= chip_val
				self.main_game.logic.cash_current += chip_val
		else:
			self.main_game.logic.cash_total += self.main_game.logic.cash_current
			self.main_game.logic.cash_current = 0

		self.main_game.logic.main_game.creation_object()
		self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current), str(self.main_game.logic.cash_total))
		self.main_game.logic.create_sc_buttons('bit')

	def mouse_event_click_bit(self, mouse_x: int, mouse_y: int) -> None:
		if 635 <= mouse_x <= 715 and 635 <= mouse_y <= 715:
			self.main_game.logic.start_game = True
			self.main_game.logic.main_game.creation_object()
			self.main_game.logic.create_sc_text('player', str(self.main_game.logic.cash_current), str(self.main_game.logic.cash_total))
			self.main_game.logic.create_sc_buttons('game')
			print('Start Game')

	def mouse_event_click_game(self, mouse_x: int, mouse_y: int) -> None:
		if 585 <= mouse_x <= 665 and 635 <= mouse_y <= 715:
			self.main_game.logic.player_add = True
		elif 685 <= mouse_x <= 765 and 635 <= mouse_y <= 715:
			self.main_game.logic.player_pass = True
