from json import load
from typing import Dict

from game import Game


if __name__ == '__main__':
	try:
		with open('settings.json', 'r') as file:
			settings: Dict = load(file)
	except FileNotFoundError as e:
		print(e)
	else:
		settings.update({"version_app": "v.0.1"})
		start_game = Game(settings)
