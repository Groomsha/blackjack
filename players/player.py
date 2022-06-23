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

from players.base import Base
from creation.creation_button import CreationButton


class Player(Base):
	def __init__(self, sc: Any) -> None:
		"""Клас для логіки гравця"""
		super(Player, self).__init__(sc)

		self.logic.create_sc_text('player', str(self.cash_current), str(self.cash_total))
		self.logic.create_sc_buttons('bit')

	def current_rate(self, chip_val: int) -> None:
		if not chip_val == -1:
			temp = self.cash_total - chip_val

			if temp >= 0:
				self.cash_total -= chip_val
				self.cash_current += chip_val
		else:
			self.cash_total += self.cash_current
			self.cash_current = 0

		self.logic.main_game.creation_object()
		self.logic.create_sc_text('player', str(self.cash_current), str(self.cash_total))
		self.logic.create_sc_buttons('bit')

	def mouse_event_click_bit(self, mouse_x: int, mouse_y: int) -> None:
		if 635 <= mouse_x <= 715 and 635 <= mouse_y <= 715:
			self.start_game = True
			self.logic.main_game.creation_object()
			self.logic.create_sc_text('player', str(self.cash_current), str(self.cash_total))
			self.logic.create_sc_buttons('game')
			print('Start Game')

	def mouse_event_click_game(self, mouse_x: int, mouse_y: int) -> None:
		if 585 <= mouse_x <= 665 and 635 <= mouse_y <= 715:
			self.player_add = True
		elif 685 <= mouse_x <= 765 and 635 <= mouse_y <= 715:
			self.player_pass = True
