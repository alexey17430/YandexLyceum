class Weapon:
    def __init__(self, name, damage, radius):
        self.name = name
        self.damage = damage
        self.radius = radius

    def hit(self, actor, target):
        if target.hp <= 0:
            print('Враг уже повержен')
        elif ((target.pos_x - actor.pos_x) ** 2 +
              (target.pos_y - actor.pos_y) ** 2) ** 0.5 > self.radius:
            print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
            target.get_damage(self.damage)

    def __str__(self):
        return self.name

    def get_name(self):
        return 'Weapon'


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_name(self):
        return 'BaseCharacter'

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if target.get_name() == 'MainHero':
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def get_name(self):
        return 'BaseEnemy'

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.all_weapon = list()
        self.weapon_now = 0
        self.next_weapon_index = 1

    def get_name(self):
        return 'MainHero'

    def hit(self, target):
        if len(self.all_weapon) == 0:
            print('Я безоружен')
        else:
            if target.get_name() == 'BaseEnemy':
                self.weapon_now.hit(self, target)
            else:
                print('Могу ударить только Врага')

    def add_weapon(self, weapon):
        try:
            if weapon.get_name() == 'Weapon':
                if len(self.all_weapon) == 0:
                    self.weapon_now = weapon
                self.all_weapon.append(weapon)
                print(f'Подобрал {weapon}')
            else:
                print('Это не оружие')
        except AttributeError:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.all_weapon) == 0:
            print('Я безоружен')
        elif len(self.all_weapon) == 1:
            print('У меня только одно оружие')
        else:
            if self.next_weapon_index == len(self.all_weapon):
                self.next_weapon_index = 0
            self.weapon_now = self.all_weapon[self.next_weapon_index]
            self.next_weapon_index += 1
            print(f'Сменил оружие на {self.weapon_now}')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')
