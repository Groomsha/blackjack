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

from typing import Any, Dict

from creation.creation_base import CreationBase


class CreationChips(CreationBase):
	def __init__(self, sc: Any) -> None:
		"""Клас створює фішки у грі"""
		super(CreationChips, self).__init__(sc)
		self.__chips_dict: Dict = {}

	@property
	def chips_dict(self) -> Dict:
		"""Get повертає Dict з об'єктами фішок"""
		return self.__chips_dict

	def _creation_sprite_to_sc(self, settings: Dict):
		"""Метод створює Dict з об'єктами фішок"""
		for key, val in settings.items():
			sprite = self._sprite_area.get_current_sprite('chips', 'all')
			self.__chips_dict.update({f'{key}': sprite})
			self._sc_main.blit(self.__chips_dict.get(key), val['pos'])
