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

import random
from typing import List, Tuple


class CreationDeck:
	def __init__(self) -> None:
		"""Створення ігрової колоди"""
		self.__shuffled_deck: Tuple = ()
		self.__suits: List = ['clubs', 'peaks', 'timbrel', 'worms']
		self.__values: List = ['2','3','4','5','6','7','8','9','10','V','D','K','A']

	@property
	def shuffled_deck(self):
		"""Get повертає Tuple з восьмі тасованих колод"""
		return self.__shuffled_deck

	def __deck_building(self) -> Tuple:
		"""створення однієї повної колоди"""
		one_deck = tuple()

		for v in self.__values:
			for s in self.__suits:
				one_deck += (s, v),

		return one_deck

	def update_shuffled(self):
		temp_deck: Tuple = tuple()

		for x in range(1, 9):
			temp_deck += self.__deck_building()

		self.__shuffled_deck = tuple(random.sample(temp_deck, len(temp_deck)))
