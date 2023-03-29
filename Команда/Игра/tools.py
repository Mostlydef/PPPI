from item import Item
from block import Block


class Tool(Item):

    def __init__(self, efficiency, name, sprite):
        self.efficiency = efficiency
        super(Tool, self).__init__(name, sprite)

    def break_block(self, block: Block):
        pass


class Pickaxe(Tool):

    def __init__(self, efficiency, name, sprite):
        super(Pickaxe, self).__init__(efficiency, name, sprite)

    def break_block(self, block: Block):
        pass


class Shovel(Tool):

    def __init__(self, efficiency, name, sprite):
        super(Shovel, self).__init__(efficiency, name, sprite)

    def break_block(self, block: Block):
        pass


class Multitool(Tool):

    def __init__(self, efficiency, name, sprite):
        super(Multitool, self).__init__(efficiency, name, sprite)

    def break_block(self, block: Block):
        pass
