class Game():
    """
    This class models a game board that plays a game of tic tac toe.
    """
    def __init__(self):
        """
        Initializes the game.
        self.board: the tic tac toe board
        self.moves: the possible moves given the gameboard
        board serialization: each square on the baord mapped to an index in a list. Displayed below:
            0 1 2
            3 4 5
            6 7 8
        """
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        
    def move(self, square, x_o):
        """
        Represents a single move on the board.
        square: the square to make the move
        x_o: x or o, the piece used
        return: No return value
        """
        if self.board[square-1] in self.moves:
            self.board[square-1] = x_o
            self.moves.remove(str(square))
        else:
            raise Exception('Square taken')
        
        
    def game_state(self):
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
        elif not self.moves: return 'c'                                           # no winner
        else: return 'n'                                                          # continue playing
        
        
    def __repr__(self):
        """
        return: string representation of the tic tac toe board
        """
        return '_______\n|{} {} {}|\n|{} {} {}|\n|{} {} {}|\n-------'.format(*self.board)
    
        
    def reset(self):
        """
        Resets the game board.
        return: no return value
        """
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        
        
        
        
        
        
        
        
        
        