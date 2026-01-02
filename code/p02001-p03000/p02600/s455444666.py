import sys, math
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    X = ii()
    X = X//100
    if 4 <= X < 6:
        print(8)
    elif 6 <= X < 8:
        print(7)
    elif 8 <= X < 10:
        print(6)
    elif 10 <= X < 12:
        print(5)
    elif 12 <= X < 14:
        print(4)
    elif 14 <= X < 16:
        print(3)
    elif 16 <= X < 18:
        print(2)
    elif 18 <= X < 20:
        print(1)

if __name__ == '__main__':
    main()