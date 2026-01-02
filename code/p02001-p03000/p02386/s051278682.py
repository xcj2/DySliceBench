#! python3
# diceIV.py - サイコロを転がす動きをシミュレートするプログラム
import sys

def getKeyFromValue(dice, value):
    keys = [k for k, v in dice.items() if v == value]
    if keys:
        return keys[0]
    return None

def initDice(numbers):  # サイコロオブジェクトに値を入れる
        # サイコロオブジェクトを定義, 配列の数値を、各面にわたす
    dice = {'top': numbers[0], 'bottom': numbers[5], 'front': numbers[1],
            'back': numbers[4], 'right': numbers[2], 'left': numbers[3]}
    return dice


def rollDice(dice, direction):  # サイコロを転がしたときの関数
    if direction == 'N':
        top = dice['front']
        bottom = dice['back']
        front = dice['bottom']
        back = dice['top']
        dice['top'] = top
        dice['bottom'] = bottom
        dice['front'] = front
        dice['back'] = back
    elif direction == 'S':
        top = dice['back']
        bottom = dice['front']
        front = dice['top']
        back = dice['bottom']
        dice['top'] = top
        dice['bottom'] = bottom
        dice['front'] = front
        dice['back'] = back
    elif direction == 'E':
        top = dice['left']
        bottom = dice['right']
        right = dice['top']
        left = dice['bottom']
        dice['top'] = top
        dice['bottom'] = bottom
        dice['right'] = right
        dice['left'] = left
    elif direction == 'W':
        top = dice['right']
        bottom = dice['left']
        right = dice['bottom']
        left = dice['top']
        dice['top'] = top
        dice['bottom'] = bottom
        dice['right'] = right
        dice['left'] = left
    return dice


def spinDice(dice):
    front = dice['right']
    right = dice['back']
    back = dice['left']
    left = dice['front']
    dice['front'] = front
    dice['right'] = right
    dice['back'] = back
    dice['left'] = left
    return dice

def assertDice(dice_1, dice_2):
    if dice_1 == dice_2:
        print('No')
        sys.exit()

# 一つの目でやるチェックをまとめる
def checkDice(dice_1,dice_2):
    assertDice(dice_1, dice_2)
    for i in range(3):
        dice_1 = spinDice(dice_1)
        assertDice(dice_1, dice_2)

def diceIII(dice_1, dice_2):
    checkDice(dice_1,dice_2)

    roll_directions = [['N'], ['S'], ['W'],['E'],['N','N']]

    dice_1 = initDice(numbers_1)

    for direction in roll_directions:
        for d in direction:
            dice_1 = rollDice(dice_1, d)
        checkDice(dice_1,dice_2)
        dice_1 = initDice(numbers_1)

n = int(input())
all_dice_numbers = []
for i in range(n):
  numbers = [int(i) for i in input().split()]
  all_dice_numbers.append(numbers)

for i in range(n):
  numbers_1 = all_dice_numbers[i]
  dice_1 = initDice(numbers_1)

  for j in range(i+1, n):
    if j == n:
      pass
    else :
      numbers_2 = all_dice_numbers[j]
      dice_2 = initDice(numbers_2)
      diceIII(dice_1, dice_2)

print('Yes')
