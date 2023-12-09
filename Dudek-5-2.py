import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        
        self.buttons = [[None for _ in range(5)] for _ in range(5)]
        
        for i in range(5):
            for j in range(5):
                self.buttons[i][j] = tk.Button(self.master, text='', font=('normal', 20), width=4, height=2,
                                              command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][4-i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(5) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(5):
            for j in range(5):
                self.board[i][j] = ' '
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()