class Achievement:
    """Реализация достижений."""
    def __init__(self, name, condition, description):
        """
        :param name: Название достижения.
        :param condition: Условие выполнения достижения.
        :param description: Описание.
        """
        self.name = name
        self.condition = condition
        self.description = description

    def check_condition(self):
        """
        Проверка условия выполнения достижения.
        """
        pass

    def achieve(self):
        """
        Выполнение достижения.
        """
        pass
