from board import TicTacToe_Board

#Player 1
#Player 2 [if needed]
class player :

    def __init__(self, player_symbol, board):
        self.player_symbol = player_symbol
        self.board = board

    def choose(self, Empty_place) :
        x, y = Empty_place
        self.board.board[x-1][y-1] = self.player_symbol



#Player 2
class ComputerPlayer(player) :

    def __init__(self, player_symbol, board):
        super().__init__(player_symbol, board)

    def choose(self) :
        x, y = random.choice(self.board.Empty_places())
        self.board.board[x-1][y-1] = self.player_symbol

    

if __name__ == "__main__":
    
    board = TicTacToe_Board()
    board.display_board()
    player1_symbol = random.choice(["X", "0"])
    player2_symbol = "0" if player1_symbol == "X" else "X"
    print("-//-"*5)
    print("Lets Start the Game")
    print("PLAYER1 SYMBOL -", player1_symbol)
    print("PLAYER2 SYMBOL -", player2_symbol)
    print("Player1 is the human player")
    print("Player2 is the Computer player (Not AI)")
    print("-//-"*5)
    player1 = player(player1_symbol, board)
    player2 = ComputerPlayer(player2_symbol, board)
    start_turn = random.randrange(2, 5)
    start_turn_player = "Player1" if start_turn%2 else "Player2"
    print(start_turn_player, "won the TOSS, And gets to choose FIRST")
    print("Firstly, it's", start_turn_player, "turn")
    turn = 0
    while not (board.GameOver() or board.checkWinner()) and turn < 9:
        turn += 1
        print("TURN -", turn)
        if start_turn_player == "Player1" and turn % 2:
            print("It's Player1's turn")
            r_n = int(input("Enter Row Number"))
            c_n = int(input("Enter Column Number"))
            if r_n in [1, 2, 3] and c_n in [1, 2, 3]:
                player1.choose((r_n, c_n))
            else:
                print("Given INVALID row and column numbers")
                turn -= 1
        elif start_turn_player == "Player1" and turn % 2 == 0:
            print("It's Player2's turn")
            player2.choose()
        elif start_turn_player == "Player2" and turn % 2 == 0:
            print("It's Player1's turn")
            r_n = int(input("Enter Row Number"))
            c_n = int(input("Enter Column Number"))
            if r_n in [1, 2, 3] and c_n in [1, 2, 3]:
                player1.choose((r_n, c_n))
            else:
                print("Given INVALID row and column numbers")
                turn -= 1
        elif start_turn_player == "Player2" and turn % 2:
            print("It's Player2's turn")
            player2.choose()
        board.display_board()
        if board.checkWinner() :
            print("The Winner is", "Player1" if board.checkWinner() == player1_symbol else "Player2")
        elif board.GameOver():
            print("It's a tie")
