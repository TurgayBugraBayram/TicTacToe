import tkinter as tk
from tkinter import messagebox


class ScoreBoard:
    def __init__(self, root):
        self.root = root
        self.x_score = 0
        self.o_score = 0

        self.x_label = tk.Label(root, text="X Score: 0", font=(None, 14))
        self.o_label = tk.Label(root, text="O Score: 0", font=(None, 14))

        self.x_label.grid(row=3, column=0, columnspan=3)
        self.o_label.grid(row=4, column=0, columnspan=3)

    def update_scores(self, winner):
        if winner == "X":
            self.x_score += 1
        elif winner == "O":
            self.o_score += 1

        self.x_label.config(text=f"X Score: {self.x_score}")
        self.o_label.config(text=f"O Score: {self.o_score}")


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        icon = tk.PhotoImage(file="TicTacToe_icon_image.png")
        self.root.iconphoto(False, icon)
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root, text="", font=("Helvetica", 20), width=6, height=2,
                    command=lambda i=i, j=j: self.make_move(i, j)
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.score_board = ScoreBoard(root)
        self.player_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.player_label.grid(row=5, column=0, columnspan=3)
        self.update_player_label()

    def update_player_label(self):
        player_label_text = f"Current Player: {self.current_player}"
        player_label_color = "red" if self.current_player == "X" else "blue"
        self.player_label.config(text=player_label_text, fg=player_label_color)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.score_board.update_scores(self.current_player)
                self.clear_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "It's a draw!")
                self.clear_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_player_label()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def clear_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = ""


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
