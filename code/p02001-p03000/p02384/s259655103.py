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

  def getRightFace(self, t, b):
    top = self.faces['top']
    back = self.faces['back']
    right = self.faces['right']
    left = self.faces['left']
    front = self.faces['front']
    bottom = self.faces['bottom']

    if t == self.getNum(2):
      self.rotate('N')

    elif t == self.getNum(4):
      self.rotate('E')

    elif t == self.getNum(5):
      self.rotate('S')

    elif t == self.getNum(3):
      self.rotate('W')

    elif t == self.getNum(6):
      for _ in range(2):
        self.rotate('N')

    while self.getFace('back') != b:
      self.rotate('R')

    result = self.getFace('right')
      
    self.faces['top'] = top
    self.faces['back'] = back
    self.faces['right'] = right
    self.faces['left'] = left
    self.faces['front'] = front
    self.faces['bottom'] = bottom

    return result

  def rotate(self, direction):
    if direction == 'N': # 前回り
      top = self.getFace('top') #一時保存

      self.faces['top'] = self.faces['back']
      self.faces['back'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['front']
      self.faces['front'] = top
      
    elif direction == 'E': # 右回り
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['left']
      self.faces['left'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['right']
      self.faces['right'] = top
      
    elif direction == 'S': # 後ろ回り
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['front']
      self.faces['front'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['back']
      self.faces['back'] = top
      
    elif direction == 'W': # 左回り
      top = self.faces['top'] #一時保存

      self.faces['top'] = self.faces['right']
      self.faces['right'] = self.faces['bottom']
      self.faces['bottom'] = self.faces['left']
      self.faces['left'] = top
      
    elif direction == 'R': # その場右回り
      back = self.faces['back'] #一時保存

      self.faces['back'] = self.faces['left']
      self.faces['left'] = self.faces['front']
      self.faces['front'] = self.faces['right']
      self.faces['right'] = back
      
    else: # その場左回り
      back = self.faces['back'] #一時保存

      self.faces['back'] = self.faces['right']
      self.faces['right'] = self.faces['front']
      self.faces['front'] = self.faces['left']
      self.faces['left'] = back
      
def main():
  number = list(map(int, input().split()))
  q = int(input())

  dice = Dice(number)

  for _ in range(q):
    t, b = map(int, input().split())
    print(dice.getRightFace(t,b))

if __name__ == '__main__':
  main()
