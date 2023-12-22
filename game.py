import random
from decouple import config


def play():
    my_money = int(config('MY_MONEY', 1000))

    while my_money > 0:
        try:
            print(f"Твой баланс: ${my_money}")
            bet = int(input("Сделай ставку: "))

            if my_money < bet:
                print(f'Вам не хватает {bet - my_money}')
            elif bet <= 0:
                print('Нельзя делать ставки ниже 1')
            else:
                win = random.randint(1, 10)

                if int(input(f"Выберите слот (1-10): ")) == win:
                    my_money += 2 * bet
                    print(f"Отлично! Вы выиграли ${2 * bet}")
                else:
                    my_money -= bet
                    print(f"Вы проиграли ${bet}. Ха лох!")

                play_again = input("Вы хотите продолжить игру? (да/yes, если вы напишите другое, то игра остановится): ").lower()
                if play_again == 'yes' or play_again == 'да':
                    pass
                else:
                    print('Такой команды не существует')
                    break
        except ValueError as error:
            print('Нужно указать цифры')


    print(f"Игра окончена! Ваш баланс: ${my_money}")
    if my_money == 0:
        print('Вы проиграли всю сумму')
    elif my_money > 1000:
        count = my_money - 1000
        print(f'Вы в плюсе на {count}')
    elif my_money == 1000:
        print('Вы ушли в 0')
    else:
        count = 1000 - my_money
        print(f'Вы ушли в минус на {count}')