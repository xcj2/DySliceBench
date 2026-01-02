#! python3
# diceII.py - サイコロを転がす動きをシミュレートするプログラム 今度はトップとフロントが与えられたときの右

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

def retrunRight(dice, first, second):  # サイコロのトップと前面の2つの値を受け取る
    first = getKeyFromValue(dice, first)
    second = getKeyFromValue(dice, second)
    if first == 'top':
        if second == 'front':
            right = dice['right']
        elif second == 'right':
            right = dice['back']
        elif second == 'back':
            right = dice['left']
        elif second == 'left':
            right = dice['front']
    elif first == 'bottom':
        if second == 'front':
            right = dice['left']
        elif second == 'left':
            right = dice['back']
        elif second == 'back':
            right = dice['right']
        elif second == 'right':
            right = dice['front']
    elif first == 'right':
        if second == 'front':
            right = dice['bottom']
        elif second == 'bottom':
            right = dice['back']
        elif second == 'back':
            right = dice['top']
        elif second == 'top':
            right = dice['front']
    elif first == 'left':
        if second == 'front':
            right = dice['top']
        elif second == 'top':
            right = dice['back']
        elif second == 'back':
            right = dice['bottom']
        elif second == 'bottom':
            right = dice['front']
    elif first == 'front':
        if second == 'top':
            right = dice['left']
        elif second == 'left':
            right = dice['bottom']
        elif second == 'bottom':
            right = dice['right']
        elif second == 'right':
            right = dice['top']
    elif first == 'back':
        if second == 'top':
            right = dice['right']
        elif second == 'right':
            right = dice['bottom']
        elif second == 'bottom':
            right = dice['left']
        elif second == 'left':
            right = dice['top']
    return right


numbers = [int(i) for i in input().split()]
dice = initDice(numbers)
q = int(input())

for i in range(q):
    first, second = [int(i) for i in input().split()]
    right = retrunRight(dice, first,second)
    print(right)
