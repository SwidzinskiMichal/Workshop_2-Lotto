import random


def generate_numbers():
    list_of_numbers = list(range(1, 50))
    random_numbers = random.choices(list_of_numbers, k = 6)
    return random_numbers


def player_input():
    player_numbers = []
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
        
        return player_numbers 


def compare_choices(list1, list2):
    points = 0
    list1 = sorted(list1)
    list2 = sorted(list2)
    for number in range(len(list1)):
        if list1[number] == list2[number]:
            points += 1
    return points
