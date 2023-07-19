import random
from decouple import config
from logic import calculate_winnings

def play_game():
    capital = float(config('initial_capital', default=1000))

    while True:
        print(f"Ваш текущий баланс: ${capital}")

        while True:
            bet = input("Введите сумму ставки: $")
            if not bet.isdigit() or float(bet) <= 0 or float(bet) > capital:
                print("Введите корректную сумму.")
            else:
                break

        while True:
            chosen_number = input("Выберите число от 1 до 30: ")
            if not chosen_number.isdigit() or int(chosen_number) < 1 or int(chosen_number) > 30:
                print("Введите число от 1 до 30.")
            else:
                break

        winning_number = random.randint(1, 30)

        print(f"Выигрышное число: {winning_number}")

        winnings = calculate_winnings(int(chosen_number), winning_number, float(bet))
        capital += winnings
        if winnings > 0:
            print(f"Вы выиграли ${winnings}!")
        else:
            print(f"Вы проиграли ${bet}.")

        if capital <= 0:
            print("У вас закончились деньги.")
            break

        play_again = input("Хотите сыграть еще? да/нет: ")
        if play_again.lower() != "да":
            break

    if capital > config('initial_capital', cast=float, default=1000):
        print(f"Вы в выигрыше на ${capital - config('initial_capital', cast=float, default=1000)}.")
    elif capital == config('initial_capital', cast=float, default=1000):
        print("Вы закончили игру с тем же балансом.")
    else:
        print(f"Вы в проигрыше на ${config('initial_capital', cast=float, default=1000) - capital}.")