import itertools
import numpy as np
import sys
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def judge(i,j):
    if j != 0:
        if l[i][j-1] == "#":
            return True
    if j != W-1:
        if l[i][j+1] == "#":
            return True
    if i != 0:
        if l[i-1][j] == "#":
            return True
    if i != H-1:
        if l[i+1][j] == "#":
            return True
    return False

H,W = IL()
l = [input() for i in range(H)]

for i in range(H):
    for j in range(W):
        if l[i][j] == "#":
            if judge(i,j) == False:
                print("No")
                exit()
print("Yes")
