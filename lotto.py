import random


def lotto():
    player_numbers = []
    list_of_numbers = list(range(1, 50))
    chosen_numbers = random.choices(list_of_numbers, k = 6)
    while len(player_numbers) != 6:
        try:
            player_choice = int(input("Please choose a number in range 1 to 49: "))
            if player_choice >= 1 and player_choice <= 49 and player_choice not in player_numbers:
                player_numbers.append(player_choice)
            elif player_choice < 1 or player_choice > 49:
                print("Please choose a number within the range of 1 to 49.")
            elif player_choice in player_numbers:
                print("This number was already chosen, please choose again.")

        except ValueError:
            print("Sorry but you have to choose an intiger in range 1 to 49.")




lotto()
