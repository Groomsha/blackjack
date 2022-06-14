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

from typing import Any, Dict, Tuple
from creation.creation_base import CreationBase


class CreationCards(CreationBase):
	def __init__(self, sc: Any) -> None:
		"""Клас створює карти у грі"""
		super(CreationCards, self).__init__(sc)
		self.__cards_dict: Dict = {}

	@property
	def cards_dict(self) -> Dict:
		"""Get повертає Dict з об'єктами карт"""
		return self.__cards_dict

	def creation_sprite_to_sc(self, quantity: Dict) -> None:
		for key, val in quantity.items():
			sprite = self._sprite_area.get_current_sprite(val['suit'], val['value'])

			self.__cards_dict.update({f'{val["suit"]}_{val["value"]}': sprite})

			self._sc_main.blit(self.cards_dict.get(f'{val["suit"]}_{val["value"]}'), val['pos_c'])
