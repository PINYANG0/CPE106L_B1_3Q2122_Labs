import tkinter as tk
import random
import gameColors as color

class Game(tk.Frame):
   
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game")
 
        self.mainGrid = tk.Frame(
            self, bg = color.board_color, bd = 3, width = 600, height = 600
        )
        self.mainGrid.grid(pady = (110,0))
 
        self.GUI()
        self.startGame()
 
        self.mainloop()
   
   def GUI(self):
        #Initiate board
        self.tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tileFrame = tk.Frame(
                    self.mainGrid,
                    bg = color.emptyTile_color,
                    width = 160,
                    height = 160
                )
                tileFrame.grid(row = i, column = j, padx = 5, pady = 5)
                tileNum = tk.Label(self.mainGrid, bg = color.emptyTile_color)
                tileData = {"frame":tileFrame, "number": tileNum}

                tileNum.grid(row=i, column=j)
                row.append(tileData)
            self.tiles.append(row)

        scoreFrame = tk.Frame(self)
        scoreFrame.place(relx=0.5, y = 45, anchor="center")
        tk.Label(
            scoreFrame,
            text = "Score",
            font = color.scoreLabel_font
        ).grid(row=0)
        self.scoreLabel = tk.Label(scoreFrame, text = "0", font = color.score_font)
        self.scoreLabel.grid(row = 1)
 
def startGame(self):
        #Construct 4x4 matrix
        self.matrix = [[0] * 4 for _ in range(4)]

        #Summon 2 random-valued tiles
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
        self.tiles[row][col]["number"].configure(
            bg = color.tile_color[2],
            fg = color.tileNum_color[2],
            font = color.tileNum_font[2],
            text = "2"
        )
        while(self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.tiles[row][col]["frame"].configure(bg = color.tile_color[2])
        self.tiles[row][col]["number"].configure(
            bg = color.tile_color[2],
            fg = color.tileNum_color[2],
            font = color.tileNum_font[2],
            text = "2"
        )

        self.score = 0
  
  

def main():
    Game()

if __name__ == "__main__":
    main()
