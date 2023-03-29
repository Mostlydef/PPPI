import pygame
from character import Character
from world import World
from camera import Camera


class Game:
    def __init__(self, character: Character, game_world: World):
        self.game_map = game_world
        self.character = character
        self.camera = Camera()

    def run(self):
        pass

    def collide(self):
        pass

    def draw(self):
        pass

    def play_music(self):
        pass

    def change_music(self):
	pass
