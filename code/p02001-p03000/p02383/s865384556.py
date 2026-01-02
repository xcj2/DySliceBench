import math
import itertools
import sys

class Dice:
  numbers = []
  faces = {
    'top': None,
    'back': None,    
    'right': None,    
    'left': None,    
    'front': None,    
    'bottom': None,
  }

  def __init__(self, int_array):
    self.numbers = int_array
    self.faces['top'] = self.numbers[0]
    self.faces['back'] = self.numbers[1]
    self.faces['right'] = self.numbers[2]
    self.faces['left'] = self.numbers[3]
    self.faces['front'] = self.numbers[4]
    self.faces['bottom'] = self.numbers[5]

  def getNum(self, n):
    return self.numbers[n-1]

  def getFace(self, f):
    return self.faces[f]

  def rotate(self, direction):
    if direction == 'N':
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['back']
      self.faces['back'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['front']
      self.faces['front'] = top
      
    elif direction == 'E':
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['left']
      self.faces['left'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['right']
      self.faces['right'] = top
      
    elif direction == 'S':
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['front']
      self.faces['front'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['back']
      self.faces['back'] = top
      
    else:
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['right']
      self.faces['right'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['left']
      self.faces['left'] = top
      
def main():
  number = list(map(int, input().split()))
  order = input()

  dice = Dice(number)

  for o in order:
    dice.rotate(o)

  print(dice.getFace('top'))


if __name__ == '__main__':
  main()
