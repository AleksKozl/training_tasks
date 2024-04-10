import random
from monsters import MonsterBerserk, MonsterHunter
from heroes import Tank, Healer, Attacker


def one_year_of_war():
    tank = Tank("Танк Пётр")
    attacker = Attacker("Убийца Ольга")
    second_attacker = Attacker("Убийца Траур")
    healer = Healer("Монах Игнат")
    second_healer = Healer("Монах Ирэна")
    good_team = [tank, attacker, second_attacker, second_healer, healer]
    if sum([isinstance(hero, (MonsterHunter, MonsterBerserk)) for hero in good_team]) > 1:
        print("В команде героев может быть только 1 монстр!")
        return 0

    evil_names = ["Абвыргл", "Мефисто", "Драник", "Диабло", "Пусечка", "Стаут"]
    mob_warrior = MonsterBerserk("Берсерк " + random.choice(evil_names))
    mob_ranger = MonsterHunter("Рейнджер " + random.choice(evil_names))
    evil_team = [mob_warrior, mob_ranger]

    for day in range(1, 366):
        print("=" * 50 + "\nНачало дня №" + str(day) + "\n" + "=" * 50)
        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            hero.make_a_move(good_team, evil_team)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            mob.make_a_move(evil_team, good_team)

        print(f"Итоги дня сражений №{day}")
        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            print(hero)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            print(mob)

        evil_team = [mob for mob in evil_team if mob.is_alive()]
        if day % 2 == 0 and len(evil_team) < 4:
            newborn_evils = [MonsterBerserk("Берсерк " + random.choice(evil_names)),
                             MonsterHunter("Рейнджер " + random.choice(evil_names))]
            evil_team.append(random.choice(newborn_evils))

        if any([not hero.is_alive() for hero in good_team]):
            print("Вы проиграли!")
            return 0
        else:
            print("Сражение продолжается!")

    else:
        print("Вы одержали победу!")
        return 1


if __name__ == '__main__':

    count_of_wins = 0
    for year in range(1, 21):
        count_of_wins += one_year_of_war()

    print("Из 20 раз команда героев одержала", count_of_wins, "побед")
    if count_of_wins < 10:
        print("Героям нужна другая тактика, попробуйте ещё!")
    else:
        print("Герои готовы к реальному сражению, задание выполнено!")
