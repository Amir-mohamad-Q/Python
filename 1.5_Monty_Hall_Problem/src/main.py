import random

def monty_hall_game(switch_doors):
    doors = ['car','goat','goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)

        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'


def simulate_game(num_games):
    num_of_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_of_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])
    return (num_of_wins_without_switching, num_of_wins_with_switching) 



if __name__ == '__main__':
    num_of_wins_without_switchingprint,num_of_wins_with_switching = simulate_game(10000)
    print('num of wins without switchingprint: ',num_of_wins_without_switchingprint)
    print('num of wins with switching: ',num_of_wins_with_switching)