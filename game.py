import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        #this is for getting the row 0,1,2(first row). 3,4,5(second row) etc.
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc tells us which number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    #will give the sub array from 1-3 row such as 0,1,2 or 3,4,5 or 6,7,8
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    
    def available_moves(self):
        #return []
        #moves = []
        #for(i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0,'x'),(1,'x'),(2,'o')]
            #if spot == ' ':
                #moves.append(i)
        #return moves

        # can use a 1 line for loop instead -->
        return [i for i, spot in enumerate(self.board) if spot == ' ']


    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')


    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


    def winner(self, square, letter):
        #winner if 3 in a row, collumn or diagonal
        #row
        row_ind = square // 3       #how many times does 3 go into square
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check collumn
        col_ind = square % 3        #divide by 3 then take the remainder
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonal
        #this is only possible on even number (0,2,4,6,8)
        #these are the only moves possible to win a diagonal
        if square % 2 == 0:
             diagonal1 = [self.board[i] for i in [0, 4, 8]]  #left to right diagonal
             if all([spot == letter for spot in diagonal1]):
                 return True
             
             diagonal2 = [self.board[i] for i in [2, 4, 6]]  #right to left diagonal
             if all([spot == letter for spot in diagonal2]):
                 return True
 
        #if all dont return true then we dont have a winner
        return False




def play(game, x_player, o_player, print_game=True):
    #returns the winner of the name! none for a tie and winners letter
    
    if print_game:
        game.print_board_nums()

    letter = 'X'        #starting letter
    # iterate while the game still has empty squares
    # we dont have to worry about winner becasue we will return that which
    # breaks the loop

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

    
    #defien the function to make the move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square} ')
                game.print_board()
                print(' ')  #just empty line


        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter


         # alternate letters after weve made our move
        letter = 'O' if letter == 'X' else 'X' #this switches the player

    #break inbetween user and computers move
    time.sleep(0.8)





        # can also be written as
        # if letter == 'X' :
        #   letter = 'O'
        # else:
        #   letter = 'X'

    #but what if there is a winner?
    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)




