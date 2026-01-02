#! python3
# diceIII.py - サイコロを転がす動きをシミュレートするプログラム

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
        print('Yes')
        sys.exit()

# 一つの目でやるチェックをまとめる
def checkDice(dice_1,dice_2):
    assertDice(dice_1, dice_2)
    # print('dice_1', dice_1)
    for i in range(3):
        dice_1 = spinDice(dice_1)
        # print('dice_1', dice_1)
        assertDice(dice_1, dice_2)

numbers_1 = [int(i) for i in input().split()]
dice_1 = initDice(numbers_1)
numbers_2 = [int(i) for i in input().split()]
dice_2 = initDice(numbers_2)

# サイコロを転がす前に、一回目のチェック
checkDice(dice_1,dice_2)

# サイコロの面を各1回ずつトップに持ってくるには5回転がす必要がある。
# サイコロは常に初期値にしておいて、転がす回数で、出す面を変えていく2次元配列で持つ

# 出す順番は以下の通り[front, back, right, left, bottom]
roll_directions = [['N'], ['S'], ['W'],['E'],['N','N']]

# print('初期値',dice_1)
# dice_1 = rollDice(dice_1, 'N')
# print('フロントがトップ',dice_1)
# checkDice(dice_1,dice_2)
# dice_1 = initDice(numbers_1)
# print('初期値2回め',dice_1)
dice_1 = initDice(numbers_1)

for direction in roll_directions:
    for d in direction:
        dice_1 = rollDice(dice_1, d)
    checkDice(dice_1,dice_2)
    dice_1 = initDice(numbers_1)

# if top_value_key == 'top':
#     pass
# elif top_value_key == 'right':
#     dice_1 = rollDice(dice_1, 'W')
# elif top_value_key == 'left':
#     dice_1 = rollDice(dice_1, 'E')
# elif top_value_key == 'front':
#     dice_1 = rollDice(dice_1, 'N')
# elif top_value_key == 'back':
#     dice_1 = rollDice(dice_1, 'S')
# else:
#     for i in range(2):
#         dice_1 = rollDice(dice_1, 'N')

# if dice_1['front'] != dice_2_front:
#     for i in range(3):
#         dice_1 = spinDice(dice_1)
#         if dice_1['front'] == dice_2_front:
#             break

# TODO : True が出るまですべての面を一度トップに持ってきて、スピンダイスで、回して、整合性を確認する
# 1 
# スピンする
# 2 [front] をトップにする（ロールダイスのN）
# スピンする
# 3 [right] をトップにする


# print(dice_1)
# print(dice_2)

print('No')
