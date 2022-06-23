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

from sources.distribution import Distribution


class Base:
	def __init__(self, sc: Any) -> None:
		"""Базовий клас для логіки гравців"""
		self.__start_game: bool = False
		self.__logic: Any = Distribution(sc)

		self.player_score: int = 0
		self.dealer_score: int = 0

		self.player_pass: bool = False
		self.player_add: bool = False

	@property
	def logic(self) -> Distribution:
		"""Get повертає об'єкт ігрового поля"""
		return self.__logic

	@property
	def start_game(self) -> bool:
		return self.__start_game

	@start_game.setter
	def start_game(self, val: bool) -> None:
		self.__start_game = val
