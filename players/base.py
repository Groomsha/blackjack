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

from typing import Dict, Any, Tuple

import pygame


class Base:
	def __init__(self, sc: Any, settings: Dict) -> None:
		"""Базовий клас для логіки гравців"""
		self.__sc_main = sc
		self.__settings = settings

	@property
	def settings(self) -> Dict:
		"""Get повертає налаштування ігрового поля"""
		return self.__settings

	@property
	def sc_main(self) -> Any:
		"""Get повертає об'єкт ігрового поля"""
		return self.__sc_main

	def _creation_text(self, options: Tuple) -> Any:
		"""Створення тексту гравців"""
		py_text = pygame.font.Font(None, options[1])
		py_text = py_text.render(options[0], True, options[2])

		return py_text
