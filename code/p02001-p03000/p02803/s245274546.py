import math
import time
from collections import deque
from copy import deepcopy

t = time.time()
def iip():
    ret = [int(i) for i in input().split()]
    if len(ret) == 1:
        return ret[0]
    return ret

def makemaze(H, W):
    maze = []
    for i in range(H):
        s = input()
        a = []
        for c in s:
            if c == ".":
                a.append(1000)
            if c == "#":
                a.append(9999)
        maze.append(a)
        #print(maze)
    return maze

def maxroot(maze, x, y, w, h):
    sn = 0
    maxx = 0
    if maze[y][x] == 9999:
        return 0

    maze = deepcopy(maze)
    maze[y][x] = 0
    que = deque()
    que.append((y, x))


    while que:
        xy = que.pop()
        y = xy[0]
        x = xy[1]
        if maze[y][x] == 9999:
            continue

        minlist = []
        if x > 0:
            minlist.append((y, x-1))
        if y > 0:
            minlist.append((y-1, x))
        if x < w-1:
            minlist.append((y, x+1))
        if y < h-1:
            minlist.append((y+1, x))

        dd = min(maze[y][x] for y, x in minlist) + 1
        dd = min(dd, maze[y][x])
        maze[y][x] = dd

        for y, x in minlist:
            if maze[y][x] != 9999 and maze[y][x] > dd+2:
                que.append((y, x))
                sn += 1
            #print(sn)

    maxx = 0
    for line in maze:
        try:
            maxa = max([i for i in line if i < 1000])
        except:
            maxa = 0
        maxx = max(maxx, maxa)
    return maxx


def main():
    H, W = iip()
    maze = makemaze(H, W)

    maxx = 1
    for y in range(H):
        for x in range(W):
            maxx = max(maxx, maxroot(maze, x, y, W, H))
            pass

    print(maxx)
    #print(maxroot(maze, 0, 2, W, H))


main()