"""
Author: amirmohamad_Q
Date Created: 16/6/1404
description: Rock/Paper/Scissors game.
"""

import random


class RockPaperScissors():
    "Main class for the game."
    def __init__(self,player_name: str):
        self.choices: list[str]= ['rock','paper','scissors']
        self.player_name: str = player_name

    def get_player_choice(self: str) -> str:
        player_choice = input(f"enter your choice ({self.choices}) : ")

        if player_choice.lower() in self.choices:
            return player_choice
        
        print(f'you must select from {self.choices}')
        self.get_player_choice()

    def get_computer_choice(self):
        return random.choice(self.choices)
        
    def deside_winner(self,player_choice: str, computer_choice: str) -> str:
        '''Deside who is winner.

        :param player_choice : choice of payer.
        :param computer_choice : choice of computer.
        :return: return who won.
        '''
        if player_choice == computer_choice:
            return "it's a Tie! "
        
        win_combinations =[('rock','scissors'),('paper','rock'),('scissors','paper')]
        for win_com in win_combinations:
            if (player_choice == win_com[0]) & (computer_choice == win_com[1]):
                return 'Player won!'
        return 'Computer won!'

    def winner_msg(self,winner: str):
        print(winner)

    def play(self):
        '''the Main method of class where contains all other 
        methods of class and use for running the game with simple code understanding.

        - Get your choice
        - Get computer choice
        - Deside woh's winner
        - Print result
        '''
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'your choice: {player_choice}\ncomputer choice: {computer_choice}')
        winner = self.deside_winner(player_choice,computer_choice)
        self.winner_msg(winner)




if __name__ == '__main__':
    game = RockPaperScissors('amir')

    while True:
        game.play()
        continue_game: str = input('Press ane key for continue AND Q/q for quite: ')
        if continue_game.lower() == 'q':
            break 
