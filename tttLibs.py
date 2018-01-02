"""
    FileName : tttLibs.py
    Description : Various functions needed by the tictactoe.py main file to run
    Version : 1.0
    Author : Christian Weaver (Dreddsparc)
"""
import random as rnd

# Initial game state setup: Variable Declarations
GAME_FINISHED = False
play_field = [7, 8, 9, 4, 5, 6, 1, 2, 3]


def player_setup():
    """
    Basic function to setup the initial player dictionary with names, and player tokens
    and a turn indicator.

    player1 and player2 are keys pointing to sub-dictionaries with name, token and turn
    status.

    Takes no arguments and returns a dictionary as defined below

    ToDo : Add input checks to be sure name that are entered make sense
    """
    player_dict = {"player1": {'name': 'AName', 'token': 'X', 'turn': 0},
                   "player2": {'name': 'AName', 'token': 'O', 'turn': 0}}
    # Get the players names into the dictionary
    for i in range(1, 3):
        player_dict['player' + str(i)]['name'] = input("Please enter the name of player {0}: ".format(i))

    # Decide which player will start first
    player_dict['player1']['turn'] = rnd.randint(0, 1)
    player_dict['player2']['turn'] = abs(player_dict['player1']['turn'] - 1)

    return player_dict
# End player_setup()


def print_playfield(pf_list):
    """
    INPUT: a list of 9 single char/int.  should be numbers 1-9
            in order on initial game state

    OUTPUT: Draws a tic-tac-toe board with list items as current
             cell state if X or O, or a number representing a play
             selection that a player can choose to signify the move
             they wish to make on the next turn

    ToDo: Possibly make the playefield an object?
    """
    print(' _________________')
    print('|     |     |     |')
    print('|  {0}  |  {1}  |  {2}  |'.format(pf_list[0], pf_list[1], pf_list[2]))
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  {0}  |  {1}  |  {2}  |'.format(pf_list[3], pf_list[4], pf_list[5]))
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  {0}  |  {1}  |  {2}  |'.format(pf_list[6], pf_list[7], pf_list[8]))
    print('|_____|_____|_____|')
# End print_playfield(pf_list)
