import random


class Warrior:

    def __init__(self, name, hitpoints=100, damage=20, status='Alive'):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.status = status

    def hit_the_target(self, target):
        target.hitpoints -= self.damage
        print('{0} бьет по {1}. Остаток здоровья {1}: {2}HP\n' \
              .format(self.name,
                      target.name,
                      target.hitpoints
                      )
              )

    def check_status(self):
        if self.hitpoints < 1:
            self.status = 'Dead'
        return self.status


def battle(list_of_opponents):
    print('Битва началась!')
    while True:
        current_opponents = list_of_opponents.copy()

        try:
            attacker = current_opponents.pop(current_opponents.index(random.choice(current_opponents)))
            victim = random.choice(current_opponents)
            attacker.hit_the_target(victim)
            victim.status = victim.check_status()
            if victim.status == 'Dead':
                print(f'{victim.name} - погиб!\n')
                list_of_opponents.remove(victim)

        except IndexError:
            print(f'{attacker.name} - победил всех!\n'
                  f'Остаток его здоровья: {attacker.hitpoints}HP')
            break


def duel(list_of_opponents):
    print('Дуэль началась!')
    current_opponents = list_of_opponents.copy()
    current_opponents = [current_opponents.pop(current_opponents.index(random.choice(current_opponents))),
                         random.choice(current_opponents)
                         ]

    while True:
        attacker = current_opponents.pop(current_opponents.index(random.choice(current_opponents)))
        victim = random.choice(current_opponents)
        attacker.hit_the_target(victim)
        victim.status = victim.check_status()
        current_opponents.append(attacker)

        if victim.status == 'Dead':
            print(f'{attacker.name} - победил! {victim.name} погиб!\n'
                  f'Остаток здоровья {attacker.name}: {attacker.hitpoints}HP')
            list_of_opponents.remove(victim)
            break

    if len(list_of_opponents) == 1:
        print(f'\n{list_of_opponents[0].name} - победил всех!\n'
              f'Остаток его здоровья: {list_of_opponents[0].hitpoints}HP'
              )


def main():
    while True:
        warriors_numb = input('Введите кол-во воинов: ')
        if warriors_numb.isdigit():
            warriors_numb = int(warriors_numb)
            break
        else:
            print('Количество воинов должно быть целым числом\n')

    warriors = [Warrior(f'Воин {warr_numb + 1}')
                for warr_numb in range(0, warriors_numb)
                ]

    while True:
        if len(warriors) == 1:
            break

        game_mode_choice = input('\nВыберите режим битвы: \n'
                                 '1. Все против всех\n'
                                 '2. Случайная дуэль\n'
                                 'Ваш выбор (1 или 2): ')
        if game_mode_choice == '1':
            battle(warriors)
        elif game_mode_choice == '2':
            duel(warriors)
        else:
            print('Нужно ввести "1" или "2"\n')


main()
