import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Tic-Tac-ToeJam!")

playField = tk.Canvas()
playField.grid(row=0, column=0)
playFieldFont = font.Font(size=10, weight='bold')

playerPanel = tk.Canvas()
playerPanel.grid(row=0, column=1)

pFSquares = []
pfHeight = 5
pfWidth = 10
playFieldDict = {1: [1, 2, 0],
                 2: [2, 2, 1],
                 3: [3, 2, 2],
                 4: [4, 1, 0],
                 5: [5, 1, 1],
                 6: [6, 1, 2],
                 7: [7, 0, 0],
                 8: [8, 0, 1],
                 9: [9, 0, 2]}

for key in playFieldDict.keys():
    pFSquares.append(tk.Button(playField,
                               text=playFieldDict[key][0],
                               height=pfHeight,
                               width=pfWidth,
                               font=playFieldFont))
    pFSquares[key-1].grid(row=playFieldDict[key][1], column=playFieldDict[key][2])

root.mainloop()
