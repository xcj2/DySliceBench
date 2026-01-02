
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())


directions = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact


def serch(x, count):
    #print("top", x, count)

    for d in directions:
        nx = d+x
        # print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)

    return count


field = []
for i in range(3):
    field.append(acinput())

N = int(input())


def chk(x):
    for i in range(3):
        for j in range(3):
            if field[i][j] == x:
                field[i][j] = -1


for i in range(N):
    chk(II())

#print(field)

for i in range(3):
    state = False
    for j in range(3):
        if field[i][j] != -1:
            break
        if j == 2:
            print("Yes")
            sys.exit()

for j in range(3):
    state = False
    for i in range(3):
        if field[i][j] != -1:
            break
        if i == 2:
            print("Yes")
            sys.exit()

state = False
for i in range(3):
    if field[i][i] != -1:
        break
    if i == 2:
        print("Yes")
        sys.exit()



for i in range(3):
    if field[2-i][i] != -1:
        break
    if i == 2:
        print("Yes")
        sys.exit()

print("No")