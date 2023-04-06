# Author: Tsz To Chan
# GitHub username: ChrisChantszto
# Date: 3/19/2023
# Description: The Checkers object represents the game as played. The class should contain information about the board and the players. The board is initialized when the Checkers object is created.
# Player object represents the player in the game. It is initialized with player_name and checker_color that the player has chosen. The parameter piece_color is a string of value "Black" or "White".
# get_king_count - takes no parameter, returns the number of king pieces that the player has
# get_triple_king_count - takes no parameter, returns the number of triple king pieces that the player has
# get_captured_pieces_count - takes no parameter, returns the number of opponent pieces that the player has captured
# In addition to your file containing the code for the above classes, **you must also submit a file that contains unit tests for your classes. It must have at least five unit tests and use at least two different assert functions.
# Your files must be named CheckersGame.py and CheckersGameTester.py

class OutofTurn(Exception):
    '''OutOfTurn Exception'''
    pass

class InvalidSquare(Exception):
    '''InvalidSuqare Exception'''
    pass

class InvalidPlayer(Exception):
    '''InvalidPlayer Exception'''
    pass

class Checkers:
    '''Checkers object'''

    def __init__(self):
        '''init method with board, player, captured_pieces and start_game data'''
        self._board = [[None, "White", None, "White", None, "White", None, "White"],
                      ["White", None, "White", None, "White", None, "White", None],
                      [None, "White", None, "White", None, "White", None, "White"],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      ["Black", None, "Black", None, "Black", None, "Black", None],
                      [None, "Black", None, "Black", None, "Black", None, "Black"],
                      ["Black", None, "Black", None, "Black", None, "Black", None]]
        self._player = {}
        self._captured_pieces = {}
        self._start_game = False

    def captured_pieces(self, player_name):
        return self._captured_pieces[player_name]

    def create_player(self, player_name, piece_color):
        '''create player method that have two params player name and piece color'''
        self._player[player_name] = piece_color
        self._captured_pieces[player_name] = 0
        player = Player(player_name, piece_color)
        player.set_checkers_game(self)
        return player


    def play_game(self, player_name, starting_square_location, destination_square_location):
        '''play game method that have three params player_name, starting_square_location and destination_square_location to play the game
        :type player_name: object
        '''

        start_row = starting_square_location[0]
        start_column = starting_square_location[1]
        end_row = destination_square_location[0]
        end_column = destination_square_location[1]

        if end_row > 7 or end_row < 0 or end_column > 7 or end_column < 0:
            raise OutofTurn
        if not self._board[start_row][start_column]:
            raise InvalidSquare
        if player_name in self._player:
            if self._player[player_name] not in self._board[start_row][start_column]:
                raise InvalidSquare
        if (start_row + start_column) % 2 == 0 or (end_row + end_column) % 2 == 0:
            raise InvalidSquare
        if player_name not in self._player:
            raise InvalidPlayer
        if self._player[player_name] == "Black":
            self._start_game = True
        if self._board[end_row][end_column] is not None:
            raise InvalidSquare
        # if player piece color is white, if the move is valid, if the destination_square_location contains black, remove black and vice versa

        if self._player[player_name] == self._board[start_row][start_column]:
            '''Black pieces'''
            if self._player[player_name] == "Black" or self._player[player_name] == "Black_king" or self._player[player_name] == "Black_Triple_King":
                if (start_row - end_row == 1 or start_row - end_row == -1) and (end_column - start_column == 1 or end_column - start_column == -1):
                    if end_row != 0:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "Black"
                        # print(self._board[end_row][end_column])
                    elif end_row == 0:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "Black_king"
                        # print(self._board[end_row][end_column])
                    elif end_row == 7:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "Black_Triple_King"

                if (start_row - end_row == 2 or start_row - end_row == -2) and (end_column - start_column == 2 or end_column - start_column == -2):
                    if self._player[player_name] == "Black" and end_row != 0:
                        self._board[start_row][start_column] = None  #box
                        self._board[end_row][end_column] = "Black"
                        '''captured pieces'''
                        if end_column - start_column == 2:
                            self._board[start_row-1][start_column+1] = None
                        elif end_column - start_column == -2:
                            self._board[start_row-1][start_column-1] = None
                        self._captured_pieces[player_name] += 1
                        # print(self._board[end_row][end_column])
                    elif self._player[player_name] == "Black" and end_row == 0:
                        self._board[start_row][start_column] = None  # box
                        self._board[end_row][end_column] = "Black_king"
                        '''captured pieces'''
                        if end_column - start_column == 2:
                            self._board[start_row - 1][start_column + 1] = None
                        elif end_column - start_column == -2:
                            self._board[start_row - 1][start_column - 1] = None
                        self._captured_pieces[player_name] += 1
                        # print(self._board[end_row][end_column])
                    elif self._player[player_name] == "Black_king" and (start_row - end_row == 2 or start_row - end_row == -2) and (end_column - start_column == 2 or end_column - start_column == -2):
                        if end_row != 7:
                            self._board[end_row][end_column] = "Black_king"
                        elif end_row == 7:
                            self._board[end_row][end_column] = "Black_Triple_King"
                        self._board[start_row][start_column] = None
                        '''captured pieces'''
                        if start_row - end_row == 2 and end_column - start_column == 2 and "White" in self._board[start_row - 1][start_column - 1]:
                            self._board[start_row - 1][start_column + 1] = None
                        elif start_row - end_row == 2 and end_column - start_column == -2 and "White" in self._board[start_row - 1][start_column + 1]:
                            self._board[start_row - 1][start_column - 1] = None
                        elif start_row - end_row == -2 and end_column - start_column == 2 and "White" in self._board[start_row + 1][start_column - 1]:
                            self._board[start_row + 1][start_column + 1] = None
                        elif start_row - end_row == -2 and end_column - start_column == -2 and "White" in self._board[start_row + 1][start_column + 1]:
                            self._board[start_row + 1][start_column - 1] = None
                        self._captured_pieces[player_name] += 1
                    elif self._player[player_name] == "Black_king" and (start_row - end_row == 2) and end_row != 0:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "Black_king"
                        '''captured pieces'''
                        self._board[start_row + 1][start_column + 1] = None
                        self._captured_pieces[player_name] += 1
                if (start_row - end_row == 3 or start_row - end_row == -3) and (end_column - start_column == 3 or end_column - start_column == -3):
                    self._board[start_row][start_column] = None  # box
                    self._board[end_row][end_column] = "Black_Triple_King"
                    '''captured pieces'''
                    if start_row - end_row == 3 and end_column - start_column == 3:
                        self._board[start_row - 1][start_column + 1] = None
                        self._board[start_row - 2][start_column + 2] = None
                    elif start_row - end_row == 3 and end_column - start_column == -3:
                        self._board[start_row - 1][start_column - 1] = None
                        self._board[start_row - 2][start_column - 2] = None
                    elif start_row - end_row == -3 and end_column - start_column == 3:
                        self._board[start_row + 1][start_column + 1] = None
                        self._board[start_row + 2][start_column + 2] = None
                    elif start_row - end_row == -3 and end_column - start_column == -3:
                        self._board[start_row + 1][start_column - 1] = None
                        self._board[start_row + 2][start_column - 2] = None
                    self._captured_pieces[player_name] += 2
                    # print(self._board[end_row][end_column])

            '''White pieces'''
            if self._player[player_name] == "White" or self._player[player_name] == "White_king" or self._player[player_name] == "White_Triple_King":
                if (start_row - end_row == 1 or start_row - end_row == -1) and (
                        end_column - start_column == 1 or end_column - start_column == -1):
                    if end_row != 7:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "White"
                        # print(self._board[end_row][end_column])
                    elif end_row == 7:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "White_king"
                        # print(self._board[end_row][end_column])
                    elif end_row == 0:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "White_Triple_King"

                if (start_row - end_row == 2 or start_row - end_row == -2) and (
                        end_column - start_column == 2 or end_column - start_column == -2):
                    if self._player[player_name] == "White" and end_row != 7:
                        self._board[start_row][start_column] = None  # box
                        self._board[end_row][end_column] = "White"
                        '''captured pieces'''
                        if end_column - start_column == 2:
                            self._board[start_row + 1][start_column + 1] = None
                        elif end_column - start_column == -2:
                            self._board[start_row + 1][start_column - 1] = None
                        self._captured_pieces[player_name] += 1
                        # print(self._board[end_row][end_column])
                    elif self._player[player_name] == "White" and end_row == 7:
                        self._board[start_row][start_column] = None  # box
                        self._board[end_row][end_column] = "White_king"
                        '''captured pieces'''
                        if end_column - start_column == 2:
                            self._board[start_row + 1][start_column + 1] = None
                        elif end_column - start_column == -2:
                            self._board[start_row + 1][start_column - 1] = None
                        self._captured_pieces[player_name] += 1
                        # print(self._board[end_row][end_column])
                    elif self._player[player_name] == "White_king" and (
                            start_row - end_row == 2 or start_row - end_row == -2) and (
                            end_column - start_column == 2 or end_column - start_column == -2):
                        if end_row != 0:
                            self._board[end_row][end_column] = "White_king"
                        elif end_row == 0:
                            self._board[end_row][end_column] = "White_Triple_King"
                        self._board[start_row][start_column] = None
                        '''captured pieces'''
                        if start_row - end_row == 2 and end_column - start_column == 2 and "Black" in self._board[start_row - 1][start_column - 1]:
                            self._board[start_row - 1][start_column + 1] = None
                        elif start_row - end_row == 2 and end_column - start_column == -2 and "Black" in self._board[start_row - 1][start_column + 1]:
                            self._board[start_row - 1][start_column - 1] = None
                        elif start_row - end_row == -2 and end_column - start_column == 2 and "Black" in self._board[start_row + 1][start_column - 1]:
                            self._board[start_row + 1][start_column + 1] = None
                        elif start_row - end_row == -2 and end_column - start_column == -2 and "Black" in self._board[start_row + 1][start_column + 1]:
                            self._board[start_row + 1][start_column - 1] = None
                        self._captured_pieces[player_name] += 1
                    elif self._player[player_name] == "White_king" and (start_row - end_row == 2) and end_row != 0:
                        self._board[start_row][start_column] = None
                        self._board[end_row][end_column] = "White_king"
                        '''captured pieces'''
                        self._board[start_row + 1][start_column + 1] = None
                        self._captured_pieces[player_name] += 1
                    if (start_row - end_row == 3 or start_row - end_row == -3) and (
                            end_column - start_column == 3 or end_column - start_column == -3):
                        self._board[start_row][start_column] = None  # box
                        self._board[end_row][end_column] = "White_Triple_King"
                        '''captured pieces'''
                        if start_row - end_row == 3 and end_column - start_column == 3:
                            self._board[start_row - 1][start_column + 1] = None
                            self._board[start_row - 2][start_column + 2] = None
                        elif start_row - end_row == 3 and end_column - start_column == -3:
                            self._board[start_row - 1][start_column - 1] = None
                            self._board[start_row - 2][start_column - 2] = None
                        elif start_row - end_row == -3 and end_column - start_column == 3:
                            self._board[start_row + 1][start_column + 1] = None
                            self._board[start_row + 2][start_column + 2] = None
                        elif start_row - end_row == -3 and end_column - start_column == -3:
                            self._board[start_row + 1][start_column - 1] = None
                            self._board[start_row + 2][start_column - 2] = None
                        self._captured_pieces[player_name] += 2
                        # print(self._board[end_row][end_column])
                        # print(self._captured_pieces[player_name])

        return self.captured_pieces(player_name)
    def get_checker_details(self, square_location):
        '''get checker_details method that have one params square_location to see the status of the square location'''

        if not self._board[square_location[0]][square_location[1]]:
            return None
        elif square_location[0] > 7 or square_location[0] < 0 or square_location[1] > 7 or square_location[1] < 0:
            raise InvalidSquare
        return print(self._board[square_location[0]][square_location[1]])
    def print_board(self):
        '''print board method'''

        return self._board

    def game_winner(self):
        '''game winner method'''
        for key, value in self._captured_pieces.items():
            if self._captured_pieces[key] == 12:
                return print(key)
        return print("Game has not ended")


class Player:
    '''player object'''

    def __init__(self, player_name, checker_color):
        '''the init method with two params player_name and checker_color'''
        self._player_name = player_name
        self._piece_color = checker_color
        self._king_count = 0
        self._triple_king_count = 0
        self._checkers_game = None

    def set_checkers_game(self, checkers_game):
        '''set the reference to the checkers game'''
        self._checkers_game = checkers_game

    def get_king_count(self):
        '''get king count method which return the king count of the player'''
        king_count = 0
        board = self.print_board()

        if self._piece_color == "Black":
            for i in range(8):
                for j in range(8):
                    if board[i][j] == "Black_king":
                        king_count += 1
        elif self._piece_color == "White":
            for i in range(8):
                for j in range(8):
                    if board[i][j] == "White_king":
                        king_count += 1
        return king_count

    def get_triple_king_count(self):
        '''get triple king count method which return the triple king count of the player'''
        if self._piece_color == "Black":
            for i in range(8):
                for j in range(8):
                    if self.print_board()[i][j] == "Black_Triple_King":
                        self._triple_king_count += 1
        elif self._piece_color == "White":
            for i in range(8):
                for j in range(8):
                    if self.print_board()[i][j] == "White_Triple_King":
                        self._triple_king_count += 1
        return self._triple_king_count

    def get_captured_pieces_count(self):
        '''get captured pieces count that returns the total number of captured pieces count of the player'''
        if self._checkers_game is not None:
            return self._checkers_game.captured_pieces(self._player_name)
        else:
            raise ValueError("Checkers game reference is not set.")
