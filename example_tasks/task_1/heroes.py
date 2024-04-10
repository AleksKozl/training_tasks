import random
from monsters import MonsterBerserk


class Hero:

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):
        raise NotImplementedError("Метод Attack")

    def take_damage(self, damage):
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        raise NotImplementedError("Метод __str__!")


class Healer(Hero):

    """
    Класс описывающий целителя. Родитель: Hero()

    Args:
        name (str): Передаваемое значение имени героя
        target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)
        damage (int): Передаваемое значение получаемого урона
        friends (lst): Передаваемый список союзников
        enemies (lst): Передаваемый список противников

    Attribute:
        max_hp (int): Атрибут описывающий максимальное значение здоровья
        start_power (int): Атрибут описывающий стартовое значение силы

        hp (int): Атрибут содержащий текущее значение здоровья
        power (int): Атрибут содержащий текущее значение здоровья
        is_alive (bool): Атрибут описывающий текущее состояние героя

        magic_power (int): Атрибут содержащий количество магической силы героя
        friends_sort (lst): Атрибут содержащий сортированный по возрастанию атрибута hp (int) список союзников
        friendly_tanks (lst): Атрибут содержащий сортированный по возрастанию атрибута hp (int) список союзников класса Tank()
        lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)

    Methods:
        get_magic_power(): Геттер атрибута magic_power (int)

        attack(target): Метод реализующий функцию атаки цели target (obj)

        take_damage(damage): Метод реализующий функцию получения урона damage (int)

        healing(): Метод реализующий функцию исцеления target (obj)

        make_a_move(friends, enemies): Метод реализующий функцию выбора действия

    """

    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = self.get_power() * 3

    def get_magic_power(self):

        """
        Геттер атрибута magic_power (int)

        Attribute:
            magic_power (int): Атрибут содержащий количество магической силы героя

        :return: magic_power
        :rtype: int
        """

        return self.__magic_power

    def attack(self, target):

        """
        Метод реализующий функцию атаки цели target (obj).

        Особенность класса Healer():
            Множитель силы атаки: 0.5

        Args:
            target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)

        """

        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):

        """
        Метод реализующий функцию получения урона damage (int)

        Особенность класса Healer:
            Множитель получаемого урона: 1.2

        Args:
            damage (int): Передаваемое значение получаемого урона

        """

        self.set_hp(self.get_hp() - (damage * 1.2))
        super().take_damage(damage)

    def healing(self, target):

        """
        Метод реализующий функцию исцеления target (obj)

        Args:
            target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)

        """

        target.set_hp(target.get_hp() + self.get_magic_power())

    def make_a_move(self, friends, enemies):

        """
        Метод реализующий функцию выбора действия на основании friends (lst) и enemies (lst).

          Args:
            friends (lst): Передаваемый список союзников
            enemies (lst): Передаваемый список противников

        Attribute:
            friends_sort (lst): Атрибут содержащий сортированный по возрастанию атрибута hp (int) список союзников
            friendly_tanks (lst): Атрибут содержащий сортированный по возрастанию атрибута hp (int) список союзников класса Tank()
            lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)

        """

        print(self.name, ': ', end='')

        friends_sort = sorted(friends, key=lambda x: x.get_hp())

        friendly_tanks = sorted([i_tank for i_tank in friends
                                 if isinstance(i_tank, Tank)
                                 ], key=lambda i_hero: i_hero.get_hp())

        if friends_sort[0].get_hp() < 80 or friendly_tanks[0].get_hp() < 120:

            if friends_sort[0].get_hp() < 50:
                print(f'Исцеляю того, кто почти при смерти - {friends_sort[0].name}')
                self.healing(friends_sort[0])

            elif friendly_tanks[0].get_hp() < 120:
                print(f'Исцеляю самого израненного танка - {friendly_tanks[0].name}')
                self.healing(friendly_tanks[0])

            else:
                print(f'Исцеляю самого пострадавшего - {friends_sort[0].name}')
                self.healing(friends_sort[0])

        else:
            lowest_hp_enemy = min(enemies, key=lambda i_enemy: i_enemy.get_hp())
            print(f'Атакую слабейшего врага - {lowest_hp_enemy.name}')
            self.attack(lowest_hp_enemy)

        super().make_a_move(friends, enemies)

    def __str__(self):
        return f'| Имя: {self.name}; HP: {self.get_hp()}|'


class Tank(Hero):

    """
    Класс описывающий танка. Родитель: Hero()

    Args:
        name (str): Передаваемое значение имени героя
        target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)
        damage (int): Передаваемое значение получаемого урона
        friends (lst): Передаваемый список союзников
        enemies (lst): Передаваемый список противников

    Attribute:
        max_hp (int): Атрибут описывающий максимальное значение здоровья
        start_power (int): Атрибут описывающий стартовое значение силы

        hp (int): Атрибут содержащий текущее значение здоровья
        power (int): Атрибут содержащий текущее значение здоровья
        is_alive (bool): Атрибут описывающий текущее состояние героя

        defence (int): Атрибут содержащий значение брони героя
        shield_is_raised (bool): Атрибут описывающий поднят или опущен щит героя
        lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)

    Methods:
        get_defence(): Геттер атрибута defence (int)

        get_shield_status(): Геттер атрибута shield_is_raised (bool)

        set_defence(): Сеттер атрибута defence (int)

        attack(target): Метод реализующий функцию атаки цели target (obj)

        take_damage(damage): Метод реализующий функцию получения урона damage (int)

        make_a_move(friends, enemies): Метод реализующий функцию выбора действия

        shield_raising(): Метод реализующий поднятие щита / Сеттер атрибута shield_is_raised (bool)

        shield_lowering(): Метод реализующий опускание щита / Сеттер атрибута shield_is_raised (bool)

    """

    def __init__(self, name):
        super().__init__(name)
        self.__defence = 1
        self.__shield_is_raised = False

    def get_defence(self):

        """
        Геттер атрибута defence (int)

        :return: defence
        :rtype: int

        """

        return self.__defence

    def get_shield_status(self):

        """
        Геттер атрибута shield_is_raised (bool)

        :return: shield_is_raised
        :rtype: bool

        """

        return self.__shield_is_raised

    def set_defence(self, new_defence):

        """
        Сеттер атрибута defence (int)

        """

        self.__defence = new_defence

    def attack(self, target):

        """
        Метод реализующий функцию атаки цели target (obj).

        Особенность класса Tank():
            Множитель силы атаки: 0.5

        Args:
            target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)

        """

        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):

        """
        Метод реализующий функцию получения урона damage (int)

        Особенность класса Tank():
            Множитель получаемого урона: damage (int) / defence (int)

        Args:
            damage (int): Передаваемое значение получаемого урона

        """

        self.set_hp(self.get_hp() - (damage / self.get_defence()))
        super().take_damage(damage)

    def shield_raising(self):

        """
        Метод реализующий поднятие щита / Сеттер атрибута shield_is_raised (bool)
        Поднятие щита изменяет:
            defence (int) *= 2
            power (int) /= 2

        Attribute:
            shield_is_raised (bool): Атрибут описывающий поднят или опущен щит героя

        """

        self.__shield_is_raised = True
        self.set_defence(self.get_defence() * 2)
        self.set_power(self.get_power() / 2)

    def shield_lowering(self):

        """
        Метод реализующий опускание щита / Сеттер атрибута shield_is_raised (bool)
        Опускание щита изменяет:
            defence (int) /= 2
            power (int) *= 2

        Attribute:
            shield_is_raised (bool): Атрибут описывающий поднят или опущен щит героя

        """

        self.__shield_is_raised = False
        self.set_defence(self.get_defence() / 2)
        self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):

        """
        Метод реализующий функцию выбора действия на основании friends (lst) и enemies (lst).

        Args:
            friends (lst): Передаваемый список союзников
            enemies (lst): Передаваемый список противников

        Attribute:
            lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)

        """

        print(self.name, ': ', end='')

        if self.get_hp() < 80 and self.get_shield_status() is False:
            self.shield_raising()
            print('Поднимаю щит!')

        elif self.get_hp() > 80 and self.get_shield_status() is True:
            self.shield_lowering()
            print('Опускаю щит!')

        else:
            lowest_hp_enemy = min(enemies, key=lambda i_enemy: i_enemy.get_hp())
            print(f'Атакую слабейшего врага - {lowest_hp_enemy.name}')
            self.attack(lowest_hp_enemy)

    def __str__(self):
        return (f'| Имя: {self.name}; | HP: {self.get_hp()}|\n'
                f'| Броня: {self.get_defence()}; | Щит поднят: {self.get_shield_status()}|')


class Attacker(Hero):

    """
    Класс описывающий убийцу. Родитель: Hero()

    Args:
        name (str): Передаваемое значение имени героя
        target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)
        damage (int): Передаваемое значение получаемого урона
        friends (lst): Передаваемый список союзников
        enemies (lst): Передаваемый список противников

        new_coefficient (int): Передаваемое значение множителя силы героя

    Attribute:
        max_hp (int): Атрибут описывающий максимальное значение здоровья
        start_power (int): Атрибут описывающий стартовое значение силы

        hp (int): Атрибут содержащий текущее значение здоровья
        power (int): Атрибут содержащий текущее значение здоровья
        is_alive (bool): Атрибут описывающий текущее состояние героя

        power_multiply (int): Атрибут содержащий значение множителя силы героя
        enemy_berserks (list): Атрибут содержащий список объектов класса MonsterBerserk противника
                               с самым низким значением атрибута hp (int)
        lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)


    Methods:
        get_power_multiply(): Геттер атрибута power_multiply (int)

        set_power_multiply(): Сеттер атрибута power_multiply (int)

        attack(target): Метод реализующий функцию атаки цели target (obj)

        take_damage(damage): Метод реализующий функцию получения урона damage (int)

        make_a_move(friends, enemies): Метод реализующий функцию выбора действия

        power_multiply_raising(): Метод реализующий увеличение атрибута power_multiply (int)

        power_multiply_lowering(): Метод реализующий уменьшение атрибута power_multiply (int)
    """

    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 1

    def get_power_multiply(self):

        """
        Геттер атрибута power_multiply (int)

        :return: power_multiply
        :rtype: int

        """

        return self.__power_multiply

    def set_power_multiply(self, new_coefficient):

        """
        Cеттер атрибута power_multiply (int)

        Args:
            new_coefficient (int): Передаваемое значение множителя силы героя

        Attribute:
            power_multiply (int): Атрибут содержащий значение множителя силы героя

        """

        self.__power_multiply = new_coefficient

    def attack(self, target):

        """
        Метод реализующий функцию атаки цели target (obj).

        Особенность класса Attacker():
            Множитель силы атаки: power_multiply (int)
            После атаки значение силы уменьшается вдвое с помощью метода power_multiply_lowering()

        Args:
            target (obj): Передаваемый в качестве цели для выбранного действия объект (союзник/противник)

        """

        target.take_damage(self.get_power() * self.get_power_multiply())
        self.power_multiply_lowering()

    def take_damage(self, damage):

        """
        Метод реализующий функцию получения урона damage (int)

        Особенность класса Attacker():
            Множитель получаемого урона: power_multiply (int) / 2

        Args:
            damage (int): Передаваемое значение получаемого урона

        """

        self.set_hp(self.get_hp() - (damage * (self.get_power_multiply() / 2)))
        super().take_damage(damage)

    def power_multiply_raising(self):

        """
        Метод реализующий увеличение атрибута power_multiply (int) в 2 раза

        """

        self.set_power_multiply(self.get_power_multiply() * 2)

    def power_multiply_lowering(self):

        """
        Метод реализующий уменьшение атрибута power_multiply (int) в 2 раза

        """

        self.set_power_multiply(self.get_power_multiply() / 2)

    def make_a_move(self, friends, enemies):

        """
        Метод реализующий функцию выбора действия на основании friends (lst) и enemies (lst).

        Args:
            friends (lst): Передаваемый список союзников
            enemies (lst): Передаваемый список противников

        Attribute:
            enemy_berserks (list): Атрибут содержащий список объектов класса MonsterBerserk противника
                                   с самым низким значением атрибута hp (int)
            lowest_hp_enemy (obj): Атрибут содержащий объект противника с самым низким значением атрибута hp (int)

        """

        print(self.name, ': ', end='')

        enemy_berserks = sorted([i_healer for i_healer in enemies
                                 if isinstance(i_healer, MonsterBerserk)],
                                key=lambda i_hunter: i_hunter.get_hp()
                                )

        if self.get_power_multiply() < 2:
            print('Накапливаю усиление!')
            self.power_multiply_raising()

        elif self.get_power_multiply() >= 2:
            if len(enemy_berserks) > 0:
                print(f'Атакую слабейшего Берсерка - {enemy_berserks[0].name}')
                self.attack(enemy_berserks[0])
            else:
                lowest_hp_enemy = min(enemies, key=lambda i_enemy: i_enemy.get_hp())
                print(f'Атакую слабейшего врага - {lowest_hp_enemy.name}')
                self.attack(lowest_hp_enemy)

        elif self.get_power_multiply() >= 3:
            print('Сбрасываю лишнее усиление!')
            self.power_multiply_lowering()

        super().make_a_move(friends, enemies)

    def __str__(self):
        return (f'| Имя: {self.name}; | HP: {self.get_hp()}|\n'
                f'| Коэффициент усиления: {self.get_power_multiply()}; |')
