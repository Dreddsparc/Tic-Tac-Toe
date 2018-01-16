import random as rnd


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


class TttGame:


    def __init__(self, player_dict):
        self.player_dict = player_dict

    def get_player1_name(self):
        return self.player_dict['player1']['name']
    pass

    def get_current_player(self):
        for key in self.player_dict.keys():
            if self.player_dict[key]['turn'] == 1:
                return self.player_dict[key]


theGame = TttGame(player_setup())
print(theGame.get_player1_name())
print(theGame.get_current_player()['name'])
