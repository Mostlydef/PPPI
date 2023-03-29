from item import Item


class Armor(Item):
    """
    Реализация брони.
    """
    def __init__(self, title, sprite, defence):
        """
        :param name: Название брони.
        :param sprite: Спрайт брони.
        :param defence: Защита брони.
        """
        self.defence = defence
        super(Armor, self).__init__(name, sprite)
