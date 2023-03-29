import tools


class Block:
    """Реализация блока."""
    def __init__(self, durability, sprite, effective_tool: tools.Tool):
        """
        :param durability: Прочность блока
        :param sprite: Спрайт блока
        :param effective_tool: Эффективный инструмент
        """
        self.durability = durability
        self.sprite = sprite
        self.effective_tool = effective_tool

    def draw(self):
        """
        Отрисовка блока.
        """
        pass

    def destroy(self):
        """
        Уничтожение блока
        """
        pass
