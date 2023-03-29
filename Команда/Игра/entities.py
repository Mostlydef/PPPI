class Entity:
    """Реализация существ"""
    def __init__(self, health_point, damage, sprite, defence,
                 drop, iframe=0.1):
        """
        :param health_point: Количество очков здоровья
        :param damage: Урон
        :param sprite: Спрайт
        :param defence: Защита
        :param drop: Предметы, которые выпадают в случае смерти
        :param iframe: Длительность неуязвимости
        """
        self.health_point = health_point
        self.damage = damage
        self.sprite = sprite
        self.defence = defence
        self.drop = drop
        self.iframe = iframe

    def die(self):
        """
        Метод, отвечающий за смерть сущностей
        """
        pass

    def spawn(self):
        """
        Метод, отвечающий за появление новых сущностей
        """
        pass

    def draw(self):
        """
        Метод отрисовки
        """


class Mob(Entity):
    """Реализация враждебных сущностей"""
    def attack_player(self):
        """
        Метод атаки игрока
        """
        pass


class NPC(Entity):
    """Реализация NPC"""
    def speak(self):
        """
        Реализация разговора с NPC

        """
        pass
