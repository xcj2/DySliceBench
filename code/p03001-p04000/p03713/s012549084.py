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

def f(i, lst):
    if lst[i]:
        salaries = list(map(lambda x: f(x, lst), lst[i]))
        return max(salaries)+min(salaries)+1
    else:
        return 1

def main():
    H, W = mi()
    m = 10**100
    for h in range(H):
        S = [h*W, math.ceil((H-h)/2)*W, math.floor((H-h)/2)*W]
        m = min(max(S)-min(S), m)
    for w in range(W):
        S = [math.ceil(H/2)*w, math.floor(H/2)*w, (W-w)*H]
        m = min(max(S)-min(S), m)
    W, H = H, W
    for h in range(H):
        S = [h*W, math.ceil((H-h)/2)*W, math.floor((H-h)/2)*W]
        m = min(max(S)-min(S), m)
    for w in range(W):
        S = [math.ceil(H/2)*w, math.floor(H/2)*w, (W-w)*H]
        m = min(max(S)-min(S), m)

    print(m)



if __name__ == '__main__':
    main()