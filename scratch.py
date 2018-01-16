import tkinter as tk
from tkinter import font

# Setup the main root window and get set the name
root = tk.Tk()
root.title("Tic-Tac-ToeJam!")

# Create the canvas to place the buttons on
# Then pack into the main window
playField = tk.Canvas()
playField.pack()

# Control the font used on the buttons in playfield
playFieldFont = font.Font(size=10, weight='bold')


def eventHandler(buttonNum):
    print("Button {} Fired!".format(buttonNum))
    pFSquares[buttonNum-1].config(text='Spooge!')


pFSquares = []  # List with the actual button objects
pfHeight = 5    # Height of each Button
pfWidth = 10    # Width of each Button

# Button Defintition Dictionary
# Key is the button number as it appears on the keypad
# Value Positions are 0: Intial button text
#                     1: Row in canvas grid
#                     2: Column in canvas grid
playFieldDict = {1: [1, 2, 0],
                 2: [2, 2, 1],
                 3: [3, 2, 2],
                 4: [4, 1, 0],
                 5: [5, 1, 1],
                 6: [6, 1, 2],
                 7: [7, 0, 0],
                 8: [8, 0, 1],
                 9: [9, 0, 2]}

# Setup the playfield
for key in playFieldDict.keys():
    pFSquares.append(tk.Button(playField,
                               text=playFieldDict[key][0],
                               height=pfHeight,
                               width=pfWidth,
                               font=playFieldFont,
                               command=lambda aButton=key: eventHandler(aButton)))
    pFSquares[key-1].grid(row=playFieldDict[key][1], column=playFieldDict[key][2])


root.mainloop()
