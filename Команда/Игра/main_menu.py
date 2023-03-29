import pygame
from game import Game
from world import World
from character import Character
from settings import Settings


class MainMenu:
    def run(self):
        pass

    def create_world(self):
        pass

    def create_character(self):
        pass

    def select_character(self):
        self.character = Character.load(self.load_character())

    def select_world(self):
        self.world = World.load(self.load_world())

    def load_world(self):
        pass

    def load_character(self):
        pass

    def start_game(self):
        self.game = Game(self.character, self.world)
        self.game.run()

    def change_settings(self):
        pass


if __name__ == '__main__':
    mm = MainMenu()
    mm.run()
