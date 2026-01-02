from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


V,E = map(int,input().split())

boss = [i for i in range(V)]
height = [0 for i in range(V)]

def get_boss(index):
    if index == boss[index]:
        return index
    else:
        boss[index] = get_boss(boss[index])
        return boss[index]


def is_same_group(a,b):
    return get_boss(a) == get_boss(b)

def unite(x,y):
    boss_x = get_boss(x)
    boss_y = get_boss(y)

    if boss_x == boss_y:
        return

    if height[x] > height[y]:

        boss[boss_y] = boss_x

    elif height[x] < height[y]:

        boss[boss_x] = boss_y

    else:
        boss[boss_y] = boss_x
        height[x] += 1


for loop in range(E):
    A,B = map(int,input().split())
    unite(A,B)

num_query = int(input())

for loop in range(num_query):
    A,B = map(int,input().split())
    if is_same_group(A,B) == True:
        print("yes")
    else:
        print("no")

