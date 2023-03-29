from block import Block


class Item:
    """Реализация предмета"""
    def __init__(self, name, sprite):
        """
        :param name: Название предмета
        :param sprite: Спрайт предмета
        """
        self.name = name
        self.sprite = sprite

    def draw(self):
        """Метод отрисовки"""
        pass


class Placeable(Item):
    def __init__(self, block: Block, name, sprite):
        self.block = block
        super(Placeable, self).__init__(name, sprite)


class Material(Item):
    def __init__(self, need_for: list[Item], name, sprite):
        self.need_for = need_for
        super(Material, self).__init__(name, sprite)
