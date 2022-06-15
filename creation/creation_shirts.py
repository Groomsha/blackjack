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


class CreationShirts(CreationBase):
	def __init__(self) -> None:
		"""Клас створює сорочки у грі"""
		super(CreationShirts, self).__init__()

	def _creation_sprite_to_sc(self, quantity: Dict) -> Tuple:
		"""Метод створює Dict з об'єктом сорочка та повертає Tuple з об'єктом"""
		sprite = self._sprite_area.get_current_sprite(quantity.get('shirt'), quantity.get('color'))
		self._sprite_tuple = (sprite, quantity.get('pos_c'))

		return self._sprite_tuple

	def return_sprite_to_sc(self, quantity: Dict) -> Tuple:
		"""Метод повертає Tuple з об'єктом сорочка"""
		sprite: Tuple = self._creation_sprite_to_sc(quantity)

		return sprite
