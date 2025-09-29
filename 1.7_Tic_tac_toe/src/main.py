import random


class TicTacToe():
    def __init__(self):
        self.board = [' '] * 10
        self.player_turn = self.get_random_fist_player()
    
    def get_random_fist_player(self):
            return random.choice(['X','O'])
    
    def show_board(self):
        print('\n')
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print('-----------')
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print('-----------')
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print('\n')

    def swap_player_turn(self):
            self.player_turn = 'X' if self.player_turn == 'O' else 'O'
            return self.player_turn

    def is_board_filled(self):
            return ' ' not in self.board[1:]
    
    def fix_spot(self, cell, player):
            self.board[cell] = player
    
    def has_player_won(self, player):
            win_combinations = [
                   [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
                   [1, 4, 7], [2, 5, 8], [3, 5, 9], # columns
                   [1, 5, 9], [3, 5, 7]] # diagonals
            for combination in win_combinations:
                   if all([self.board[cell] == player for cell in combination]):
                          return True
            return False
            
    def start(self, ai=False):
           while True:
                self.show_board()
                print(f'player {self.player_turn} turn')
                input_cell = int(input('Enter a number from 1-9 :'))     

                if input_cell in range(1, 10) and self.board[input_cell] == ' ':
                    self.fix_spot(input_cell, self.player_turn)
                    
                    if self.has_player_won(self.player_turn):
                        print(f'Player {self.player_turn} won!')
                        self.show_board()
                        break

                    self.swap_player_turn()
                    if ai:
                        x = random.choice(range(1,9))
                        while self.board[x] != ' ':
                            x = random.choice(range(1,9))
                        self.fix_spot(x, self.player_turn)
                        self.swap_player_turn()

                    if self.is_board_filled():
                        print('draw!')
                        break
                else:
                    print('Invalid cell number')



if __name__ == '__main__':
    game = TicTacToe()
    game.start()