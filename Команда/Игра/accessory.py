from item import Item


class Accessory(Item):
    """Реализация аксессуаров."""
    def __init__(self, name, sprite, buff):
        """

        :param name: Название аксессуара;
        :param sprite: Спрайт аксессуара;
        :param buff: Эффект, который даёт аксессуар.
        """
        self.buff = buff
        super(Accessory, self).__init__(name, sprite)
