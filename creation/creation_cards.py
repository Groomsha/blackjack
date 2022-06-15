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

from typing import Dict, Tuple

from creation.creation_base import CreationBase


class CreationCards(CreationBase):
	def __init__(self) -> None:
		"""Клас створює карти у грі"""
		super(CreationCards, self).__init__()
		self.__cards_dict: Dict = {}

	@property
	def cards_dict(self) -> Dict:
		"""Get повертає Dict з об'єктами карт"""
		return self.__cards_dict

	def _creation_sprite_to_sc(self, quantity: Dict) -> Tuple:
		"""Метод створює Dict з об'єктом карти та повертає Tuple об'єкта"""
		sprite = self._sprite_area.get_current_sprite(quantity['suit'], quantity['value'])

		self.__cards_dict.update({f'{quantity["suit"]}_{quantity["value"]}': sprite})
		self._sprite_tuple = ((self.__cards_dict.get(f'{quantity["suit"]}_{quantity["value"]}'), quantity['pos_c']))

		return self._sprite_tuple

	def return_sprite_to_sc(self, quantity: Dict) -> Tuple:
		"""Метод повертає Tuple з об'єктом карти"""
		sprite: Tuple = self._creation_sprite_to_sc(quantity)

		return sprite
