from entities import Entity
from block import Block
from character import Character


class World:

    def __init__(self, character: Character, entities: list[Entity], blocks: list[list[Block]]):
        self.character = character
        self.entities = entities
        self.blocks = blocks

    def draw(self):
        pass

    @classmethod
    def load(cls, data):
        pass
