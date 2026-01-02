import math
import itertools
import sys

class Dice:
  def __init__(self, int_array):
    self.numbers = int_array
    self.faces = {}
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
      
    elif direction == 'L': # その場左回り
      back = self.faces['back'] #一時保存

      self.faces['back'] = self.faces['right']
      self.faces['right'] = self.faces['front']
      self.faces['front'] = self.faces['left']
      self.faces['left'] = back

def isSameDice(dice_1, dice_2):
  faces = ['top', 'back', 'right', 'left', 'front', 'bottom']

  for _ in range(4):
    for _ in range(4):
      flag = True

      for face in faces:
        if dice_1.getFace(face) != dice_2.getFace(face):
          flag = False
          break

      if flag:
        return True
      dice_1.rotate('R')

    dice_1.rotate('N')

  dice_1.rotate('E')
  for _ in range(4):
    flag = True

    for face in faces:
      if dice_1.getFace(face) != dice_2.getFace(face):
        flag = False
        break

    if flag:
      return True
    dice_1.rotate('R')

  for _ in range(2):
    dice_1.rotate('W')
  for _ in range(4):
    flag = True

    for face in faces:
      if dice_1.getFace(face) != dice_2.getFace(face):
        flag = False
        break

    if flag:
      return True
    dice_1.rotate('R')

  return False
      
def main():
  n = int(input())
  dices = [list(map(int, input().split())) for _ in range(n)]

  existSame = False

  for c in itertools.combinations(dices, 2):
    if isSameDice(Dice(c[0]), Dice(c[1])):
      existSame = True
      break

  if existSame:
    print('No')
  else:
    print('Yes')

if __name__ == '__main__':
  main()
