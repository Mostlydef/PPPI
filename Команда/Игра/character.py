from inventory import Inventory
from armor import Armor
from accessory import Accessory


class Character:
    """
    Реализация игрового персонажа.
    """
    def __init__(self, health_point, mana_point, inventory: Inventory,
                 armor: list[Armor], accessories: list[Accessory], iframe=0.1):
        """
        :param health_point: Количество очков здоровья
        :param mana_point: Количество очков маны
        :param inventory: Инвентарь
        :param armor: Броня
        :param accessories: Аксессуары
        :param iframe: Длительность времени неуязвимости
        """
        self.health_point = health_point
        self.mana_point = mana_point
        self.iframe = iframe

        self.inventory = inventory
        self.defence = 0
        self.armor = armor
        self.accessories = accessories

    def left_click(self):
        """
        Действие при нажатии ЛКМ
        """
        pass

    def right_click(self):
        """
        Действие при нажатии ПКМ
        """
        pass

    def move(self):
        """
        Метод передвижения
        """
        pass

    def interact_with_inventory(self):
        """
        Метод взаимодействия с инвентарём
        """
        pass

    def craft(self):
        """
        Метод создания предметов
        """
        pass

    @classmethod
    def load(cls, data):
        """
        Метод для загрузки персонажа

        :param data: Информация
        """
        pass
