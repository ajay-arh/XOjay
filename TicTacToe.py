#1initiallization of gridcells
import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["","",""],["","",""],["","",""]]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe 2-Players XOXO")

        self.gridbuttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window,text="",width=18,height=9,command= lambda i=i,j=j:self.makes_move(i,j)) #2 command adding after grid
                button.grid(row=i,column=j)
                row.append(button)
            self.gridbuttons.append(row)
    
    #2
    def makes_move(self,row,col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.gridbuttons[row][col].config(text=self.current_player) #all x are in grid
            #4 winner
            if self.check_winner(self.current_player):
                messagebox.showinfo("GAME OVER","WINNER IS "+self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("GAME OVER","GAME DRAW")
                self.window.quit()
            else:
                self.current_player= "O" if self.current_player == "X" else "X" #3 to grid xand o
            #3 to grid xand o
            #self.current_player= "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]: #rows
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]: #colm
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]: #diagnoal
            return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def run(self):
        self.window.mainloop()
xogame = TicTacToe()
xogame.run() #shows the grid button initaillization




