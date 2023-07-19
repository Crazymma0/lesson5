from decouple import config

def calculate_winnings(chosen_number, winning_number, bet):
    if chosen_number == winning_number:
        return 30 * bet
    else:
        return -bet