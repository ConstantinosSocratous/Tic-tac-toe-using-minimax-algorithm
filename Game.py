from Player import Player
import random
from math import inf as infinity


class Game:
    board = []
    currentPlayer: Player = None
    def __init__(self, human: Player, computer: Player, humanFirst: bool):
      self.human = human
      self.computer = computer
      self.initGame()
      self.humanPlaysFirst(humanFirst)

    def initGame(self):
      """
      Init the board
      """
      self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def print(self):
      print()
      print("Player", self.currentPlayer.name, "plays")
      for i in range(3):
        for j in range(3):
          print("|", self.board[i][j], end=" ")

        print("|")
        print()
      
    def appendBoard(self, i,j,value):
      """
      Add a value to the board
      """
      self.board[i][j] = value
    
    def humanPlaysFirst(self, value: bool):
      """
      Define who is going to start first
      """
      if value:
        self.currentPlayer = self.human
      else:
        self.currentPlayer = self.computer

    def takeInput(self, position):
      """
      Take an input as a number and transform it as a row and col
      """
      try:
        x = self.getRowCol(int(position))
      except:
        return False
      
      if x == -1:
        return False

      if self.board[x[0]][x[1]] == " ":
        self.appendBoard(x[0],x[1],self.currentPlayer.name)
        return True
      else:
        return False

    def takeComputerInput(self, i,j):
      """
      Take an input as a row and col
      """
      if self.board[i][j] == " ":
        self.appendBoard(i,j,self.currentPlayer.name)
        return True
      else:
        return False

    def changePlayer(self):
      """
      Set the current player 
      to the opponent of the current player
      """
      if self.currentPlayer == self.human:
        self.currentPlayer = self.computer
      else:
        self.currentPlayer = self.human
          
    def getRowCol(self, number):
      """
      Transform a number into a row and a column
      and return it
      """
      switcher = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2]
      }
      return switcher.get(number,-1)
  
    def isPlayerWinner(self,board, player):
      if self.winnerHelper(player.name):
        return True
      else:
        return False
    
    def isThereWinner(self, board):
      return self.isPlayerWinner(board,self.human) or self.isPlayerWinner(board,self.computer)

    
    def winnerHelper(self,playerName):
      if (self.board[0][0] == playerName and self.board[0][1] == playerName
       and self.board[0][2] == playerName) or (self.board[1][0] == playerName and self.board[1][1] == playerName
       and self.board[1][2] == playerName) or (self.board[2][0] == playerName and self.board[2][1] == playerName
       and self.board[2][2] == playerName) or (self.board[0][0] == playerName and self.board[1][0] == playerName
       and self.board[2][0] == playerName) or (self.board[0][1] == playerName and self.board[1][1] == playerName
       and self.board[2][1] == playerName) or (self.board[0][2] == playerName and self.board[1][2] == playerName
       and self.board[2][2] == playerName) or (self.board[0][0] == playerName and self.board[1][1] == playerName
       and self.board[2][2] == playerName) or (self.board[0][2] == playerName and self.board[1][1] == playerName
       and self.board[2][0] == playerName):
        return True
      else:
        return False

    def getOpponent(self, player):
      if player == self.human:
        return self.computer
      else:
        return self.human
    
    def isBoardFull(self,board):
      for i in range(3):
        for j in range(3):
          if board[i][j] == " ":
            return False
      return True
  
    def numOfEmptyCells(self):
      count = 0
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == " ":
            count = count + 1
      return count

    def minimax(self,board,player, depth):
      if player == self.computer:
        best = [-1, -1, -infinity]
      else:
        best = [-1, -1, +infinity]
    
      if depth == 0 or self.isThereWinner(board):
        if self.isPlayerWinner(board, self.computer):
          return [-1, -1, 1]
        elif self.isPlayerWinner(board, self.human):
          return [-1,-1,-1]
        else:
          return [-1,-1,0]
    
      for i in range(3):
        for j in range(3):
          if board[i][j] == " ":
            board[i][j] = player.name
            score = self.minimax(board, self.getOpponent(player), depth-1)
            board[i][j] = " "
            score[0], score[1] = i, j
        
            if player == self.computer:
              if score[2] > best[2]:
                  best = score
            else:
              if score[2] < best[2]:
                best = score
    
      return best
    