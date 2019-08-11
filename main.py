from Game import Game
from Player import Player
import platform
from os import system
import time
from random import choice

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def start(game: Game):
    game.print()
    while True:
        if game.currentPlayer == game.computer:
            print("AI PLAYING...")
            depth = game.numOfEmptyCells()
            if depth == 9:
                game.takeComputerInput(choice([0, 1, 2]),choice([0, 1, 2]))
            else:
                move = game.minimax(game.board,game.computer, game.numOfEmptyCells())
                game.takeComputerInput(move[0],move[1])
        else:
            print("Input cell (1-9):", end= " ")
            inpt = input()
            while not game.takeInput(inpt):
                print("Cell not empty or invalid input")
                print("Input cell (1-9):", end= " ")
                inpt = input()

        if(game.isPlayerWinner(game.board,game.currentPlayer)):
            clean()
            game.print()
            print(game.currentPlayer.name, " won")
            break 

        if game.isBoardFull(game.board):
            clean()
            game.print()
            print("Draw")
            break

        game.changePlayer()

        clean()
        game.print()

    
    print("Type y to play again:", end = " ")
    if input() == "y":
        clean()
        init()
    

def init():

    print("You want X ? [y/n]:", end=" ")
    ans = input()
    while ans != "y" and ans != "n":
        print("You want X (type 'y' for Yes and 'n' for No):", end=" ")
        ans = input()
    
    print("Start first ? [y/n]:", end=" ")
    first = input()
    while first != "y" and first != "n":
        print("Start first ?(type 'y' for Yes and 'n' for No):", end=" ")
        first = input()
    
    if first == "y":
        first = True
    else: 
        first = False

    if ans == "y":
        game = Game(Player("X"), Player("O"), first)
    else:
        game = Game(Player("O"), Player("X"), first)
    
    clean()
    time.sleep(1)
    start(game)

def main():
    init()

if __name__ == '__main__':
    main()


