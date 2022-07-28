import random
import os

class Game:
    def __init__(self):
        self.grid = [[' ' for x in range(5)] for y in range(5)]
        self.availGrid = [x for x in range(25)]
        self.playerGrid = list()
        self.botGrid = list()

    def start(self):
        os.system('cls')
        self.drawBoard()
        while True:
            self.playerTurn()
            os.system('cls')
            self.drawBoard()
            if self.checkWin(self.playerGrid):
                print('You Win!')
                break
            if not self.availGrid:
                print('Draw!')
                break
            self.botTurn()
            os.system('cls')
            self.drawBoard()
            if self.checkWin(self.botGrid):
                print('Bot Wins!')
                break
            if not self.availGrid:
                print('Draw!')
                break

    def drawBoard(self):
        [print(f'  {i}', end=' ') for i in range(5)]
        print()
        for i in range(5):
            print(' ---'*5)
            [print(f'| {self.grid[i][j]}', end=' ') for j in range(5)]
            print('| ')
        print(' ---'*5)

    def playerTurn(self):
        r = False
        while True:
            try:
                turn = int(input('Your turn please: '))
                i = 4
                while i >=0:
                    if self.grid[i][turn] != ' ':
                        i -= 1
                        continue
                    r = True
                    break
                if r:
                    self.playerGrid.append(self.availGrid.pop(self.availGrid.index(i*5 + turn)))
                    self.grid[i][turn] = 'X'
                    print(f'You play {i*5 + turn}.')
                    break

                print('Column is full! Choose another one.')
                
            except ValueError:
                print(' !Please input a number not letters or special characters.')

            except IndexError:
                print(' !Only enter a value between 0-4.')

    def botTurn(self):
        r = False
        while True:
            turn = random.randint(0,4)
            i = 4
            while i >= 0:
                if self.grid[i][turn] != ' ':
                    i -= 1
                    continue
                r = True
                break
            if r:
                self.botGrid.append(self.availGrid.pop(self.availGrid.index(i*5 + turn)))
                self.grid[i][turn] = 'O'
                print(f'Bot plays {turn}.')
                break
            
    def checkWin(self, gridList):
        winningGrid = [[0,1,2,3],
                       [1,2,3,4],
                       [5,6,7,8],
                       [6,7,8,9],
                       [10,11,12,13],
                       [11,12,13,14],
                       [15,16,17,18],
                       [16,17,18,19],
                       [20,21,22,23],
                       [21,22,23,24],
                       [0,5,10,15],
                       [5,10,15,20],
                       [1,6,11,16],
                       [6,11,16,21],
                       [2,7,12,17],
                       [7,12,17,22],
                       [3,8,13,18],
                       [8,13,18,23],
                       [4,9,14,19],
                       [9,14,19,24],
                       [5,11,17,23],
                       [0,6,12,18],
                       [6,12,18,24],
                       [1,7,13,19],
                       [3,7,11,15],
                       [4,8,12,16],
                       [8,12,16,20],
                       [9,13,17,21]
                       ]

        for com in winningGrid:
            if all([c in gridList for c in com]):
                return True

        return False

        
if __name__ == '__main__':
    g = Game()
    g.start()
