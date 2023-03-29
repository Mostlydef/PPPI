from item import Item
from entities import Entity


class Weapon(Item):

    def __init__(self, damage, knockback, attack_speed, crit_chance, name, sprite):
        self.damage = damage
        self.knockback = knockback
        self.attack_speed = attack_speed
        self.crit_chance = crit_chance

        super(Weapon, self).__init__(name, sprite)

    def attack(self, entity: Entity):
        pass


class MeleeWeapon(Weapon):

    def __init__(self, damage, knockback, attack_speed, crit_chance, attack_range, name, sprite):
        self.attack_range = attack_range
        super(MeleeWeapon, self).__init__(damage, knockback, attack_speed, crit_chance, name, sprite)

    def attack(self, entity):
        pass

    def defense(self, entity):
        pass

    def cast(self, entity):
        pass

class Projectile:
    def __init__(self, velocity, direction, is_shine, gravity):
        self.velocity = velocity
        self.direction = direction
        self.is_shine = is_shine
        self.gravity = gravity

    def move(self):
        pass


class RangedWeapon(Weapon):

    def __init__(self, damage, knockback, attack_speed, crit_chance, attack_range, name, sprite, velocity):
        self.attack_range = attack_range
        self.velocity = velocity
        super(RangedWeapon, self).__init__(damage, knockback, attack_speed, crit_chance, name, sprite)

    def attack(self, entity):
        pass


class MagicWeapon(Weapon):
    def __init__(self, damage, knockback, attack_speed, crit_chance, attack_range, name, sprite, velocity):
        self.attack_range = attack_range
        self.velocity = velocity
        super(MagicWeapon, self).__init__(damage, knockback, attack_speed, crit_chance, name, sprite)

    def attack(self, entity):
        pass


class Summon(Entity):
    def __init__(self, health_point, damage, sprite):
        super(Summon, self).__init__(health_point, damage, sprite)

    def attack(self, entity):
        pass


class SummonWeapon(Weapon):
    def __init__(self, damage, knockback, attack_speed, crit_chance, name, sprite, health_point,
                 defence, iframe, summon_sprite):
        self.summon = Summon(health_point, damage, summon_sprite, defence, iframe)
        super(SummonWeapon, self).__init__(damage, knockback, attack_speed, crit_chance, name, sprite)

    def attack(self, entity):
        pass
