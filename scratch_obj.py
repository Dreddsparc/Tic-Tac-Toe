import random as rnd


class TttGame(object):
    """
    Tic-Tac-ToeJam Main Game Object
    """
    # Class Variables
    Debug = False
    player_dict = {"player1": {'name': 'AName', 'token': 'X', 'turn': 0},
                   "player2": {'name': 'AName', 'token': 'O', 'turn': 0}}

    def __init__(self):
        pass

    @staticmethod
    def toggle_debug():
        """
        Toggle Debug flag to show or suppress extra console output while building class
        :return: Return Debug status, True if on, False if Off
        """
        if TttGame.Debug:
            TttGame.Debug = False
            print("Setting Debug to False")
        else:
            TttGame.Debug = True
            print("Setting Debug to True")
        return TttGame.Debug

    def setup_players(self):
        """
        Setup the player Dictionary class variable for use in the game
            Dict keys are 'player1', 'player2'
            Player Dict Keys are 'name', 'token', 'turn'
                name : name player entered in setup
                token: token player will use in the game (x or o)
                turn : flag that indicates if its the players turn 1 for current player 0 if not
        :return: No return value
        """
        for i in range(1, 3):
            TttGame.player_dict['player' + str(i)]['name'] = input("Please enter the name of player {0}: ".format(i))

        # Decide which player will start first
        TttGame.player_dict['player1']['turn'] = rnd.randint(0, 1)
        TttGame.player_dict['player2']['turn'] = abs(TttGame.player_dict['player1']['turn'] - 1)
        if TttGame.Debug:
            print(TttGame.player_dict)

    def get_player1_name(self):
        return TttGame.player_dict['player1']['name']

    def get_current_player(self):
        for key in self.player_dict.keys():
            if self.player_dict[key]['turn'] == 1:
                return TttGame.player_dict[key]['name']


theGame = TttGame()

theGame.toggle_debug()
theGame.setup_players()
print(theGame.get_current_player())
