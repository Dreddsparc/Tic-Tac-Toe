# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:21:31 2017

@author: Christian Weaver (Dreddsparc)
"""
import tttLibs as tttL

if __name__ == '__main__':
    # test code lines follow
    players = tttL.player_setup()
    print('Welcome to the game {0} and {1}'.format(players['player1']['name'], players['player2']['name']))
    tttL.print_playfield(tttL.play_field)
