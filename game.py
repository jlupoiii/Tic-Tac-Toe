class Game():
    """
    This class models a game board that plays a game of tic tac toe.
    """
    def __init__(self):
        """
        Initializes the game.
        self.board: the tic tac toe board
        board serialization: each square on the baord mapped to an index in a string. Displayed below:
            0 1 2
            3 4 5
            6 7 8
        """
        self.board = '123456789'

#     def s(self):
#         """
#         Gives the state of the game
#         return: The string representation of the board's state
#         """
#         return self.board
    
    
    def move(self, square, x_o):
        """
        Represents a single move on the board, changes self.board according to the move
        square: the square to make the move
        x_o: x or o, the piece used
        return: No return value
        """
        if self.board[square-1] in self.board:
            self.board = self.board[:square-1] + x_o + self.board[square:]
        else:
            raise Exception('Square taken')
        
        
    def game_step(self):
        """
        Shows the game state depending on the gameboard.
        return: 'x' if x wins
                'o' if o wins
                'c' if the game is a tie
                'n' if the game is not finished
        """
        if self.board[0]==self.board[1]==self.board[2]: return self.board[0]      # horizontals
        elif self.board[3]==self.board[4]==self.board[5]: return self.board[3]
        elif self.board[6]==self.board[7]==self.board[8]: return self.board[6]
        elif self.board[0]==self.board[3]==self.board[6]: return self.board[0]    # verticals
        elif self.board[1]==self.board[4]==self.board[7]: return self.board[1]
        elif self.board[2]==self.board[5]==self.board[8]: return self.board[2]
        elif self.board[0]==self.board[4]==self.board[8]: return self.board[0]    # diagonals
        elif self.board[2]==self.board[4]==self.board[6]: return self.board[2]
        elif all([(s in 'xo') for s in self.board]): return 'c'                   # no winner
        else: return 'n'                                                          # continue playing
    
    def reward(self):
        """
        Gives the reward for the given game state
        return: integer value of the reward
            Win: 2
            Cat: 1
            Still going: 0
        """
        if self.game_state()=='x' or self.game_state()=='o': return 2
        elif self.game_state() == 'c': return 1
        else: return 0
        
        
    def __repr__(self):
        """
        return: string representation of the tic tac toe board
        """
        return '_______\n|{} {} {}|\n|{} {} {}|\n|{} {} {}|\n-------'.format(*[s for s in self.board])
    
        
    def reset(self):
        """
        Resets the game board.
        return: no return value
        """
        self.board = '123456789'
        