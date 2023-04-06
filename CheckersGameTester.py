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

import unittest
from CheckersGame import Checkers, Player, OutofTurn, InvalidSquare, InvalidPlayer

class CheckersGameTester(unittest.TestCase):
    '''the unit test case checkersgametester'''
    def test_create_player(self):
        '''test game player'''
        game = Checkers()
        player1 = game.create_player("Adam", "White")
        self.assertEqual(player1.player_name, "Adam")
        self.assertEqual(player1.checker_color, "White")

    def test_get_checker_details(self):
        '''test the get checker details method'''
        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")
        self.assertEqual(game.get_checker_details((1, 2)), "White")

    def test_play_game_and_capture(self):
        '''test the play game and captured pieces'''
        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")
        captured_pieces = game.play_game("Lucy", (5, 6), (4, 7))
        self.assertEqual(captured_pieces, 0)

    def test_exception_invalid_player(self):
        '''test the invalid player name'''
        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")
        with self.assertRaises(InvalidPlayer):
            game.play_game("InvalidPlayer", (5, 6), (4, 7))

    def test_exception_out_of_turn(self):
        '''test the out of turn exception method'''
        game = Checkers()
        player1 = game.create_player("Adam", "White")
        player2 = game.create_player("Lucy", "Black")
        with self.assertRaises(OutofTurn):
            game.play_game("Lucy", (5, 6), (4, 7))
            game.play_game("Lucy", (5, 4), (4, 3))

if __name__ == '__main__':
    '''main'''
    unittest.main()