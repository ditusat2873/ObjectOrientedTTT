class Board:
    def __init__(self):
        self.positions = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def print_board(self):
        ''' This creates a board and puts the values of 1...9 in it.'''
        print(self.positions["1"] + "|" + self.positions["2"] + "|" + self.positions["3"] + "|")
        print("-+" * 3)
        print(self.positions["4"] + "|" + self.positions["5"] + "|" + self.positions["6"] + "|")
        print("-+" * 3)
        print(self.positions["7"] + "|" + self.positions["8"] + "|" + self.positions["9"] + "|")

    '''This function checks if the position the player places is available and returns True or False based on position'''
    def validMove(self, position):
        if self.positions[position] == " ":
            return True
        return False
    '''This function will then update the board with the position.  Before updating, it checks if the position is valid by calling validMove'''
    def boardChange(self, position, name):
        if self.validMove(position):
            self.positions[position] = name
            return self.positions
        return None
    '''This function will see if a win is made.  It will then use a for loop to check the values inside the cases.'''
    def winnerCheck(self, player):
        playerType = player.name
        runs = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["1", "5", "9"],
            ["7", "5", "3"]
        ]
        for a, b, c in runs:
            if self.positions[a] == self.positions[b] == self.positions[c] == player.name:
                print(self.print_board())
                return True
class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Player {}".format(self.name)


class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()

    '''This will just print out the numbers associated with the positions on the board.'''
    def entries(self):
        print("""
            1 - top left    | 2 - top middle    | 3 - top right
            4 - middle left | 5 - center        | 6 - middle right
            7 - bottom left | 8 - bottom middle | 9 - bottom right""")
    '''This method will print the board.'''
    def printBoard(self):

        self.board.print_board()

    """Changes the player turn.
            Receives a player and returns the other."""
    def change_turn(self, player):

        if player is self.player1:
            return self.player2
        else:
            return self.player1

    """Returns True if the player won the game, False otherwise."""
    def won_game(self, player):
        return self.board.winnerCheck(player)

    '''This will update the board and check if any positions are not available'''
    def modifyBoard(self, position, name):

        if self.board.boardChange(position, name) is not None:
            return self.board.boardChange(position, name)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.boardChange(position, name)

'''The main method in which the entire game will run'''
def play():

    game = Game()
    #Game().entries()
    game.entries()
    player = game.player1
    available = 9
    while available > 0:
        available = available-1
        game.printBoard()
        position = input("{} turn, what's your move? ".format(player))
        game.modifyBoard(position, player.name)
        if game.won_game(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = game.change_turn(player)
    if available == 0:
        print(game.board.print_board())
        print("Game over! It's a tie!")

play()
