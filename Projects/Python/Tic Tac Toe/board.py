# this file shows the TICTACTOE_BOARD class separately

class TicTacToe_Board :
    
    # Initialize the board as a 3*3 2D-List

    def __init__(self) :
        self.board = [["##" for j in range(1, 4)]for i in range(1, 4)]
    
    # Check if the given volumn value is considered as EMPTY
    def isEmpty(self, value):
        return not value in ["X", "0"]

    # Find and group all the empty holders in the board
    # Return a list containing tuples of Empty Holders
    def Empty_places(self) :
        empty = []
        for i in self.board :
            for j in i:
                if self.isEmpty(j):
                    empty.append((self.board.index(i)+1, i.index(j)+1))
        return empty

    #Check if the game passed diagonal-wise
    #Return the symbol if any 
    #Else Return False
    def diagonalpass(self) :
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ["X", "0"] :
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ["X", "0"] :
            return self.board[0][2]
        return False
    
    #Check if the game passed Column-wise
    #Return the symbol if any 
    #Else Return False
    def columnpass(self) :

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in ["X", "0"]:
                return self.board[0][i]
        return False
        
    # Checks the Winner based on rowpass, columnpass, diagonalpass
    #if the Winner is choosen the game stops
    def checkWinner(self) :
        
        if ["X", "X", "X"] in self.board : #Rowpass - "X"
            return "X"

        elif ["0", "0", "0"] in self.board : #RowPass - "0"
            return "0"

        elif (winner := self.columnpass()) :
            return winner
        
        elif (winner := self.diagonalpass()):
            return winner
        
        else:
            return False
        
    #Displaying the board
    #Prints a well-structured board till the current stage of the board
    def display_board(self) :

        for i in range(3):
            print("+"*18)
            print(("|"+(" "*4)+"|")*3)
            for j in range(3):
                print("|" + str(self.board[i][j]).center(4) + "|", end = "")
            print("**", i+1 , "**" )
            print(("|"+(" "*4)+"|")*3)
        print("+"*18)

    #Checks if the Game has completed.
    #Based on the no.of Empty - Holders
    def GameOver(self) :
        return self.Empty_places() == []
