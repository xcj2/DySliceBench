import sys, math
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
    S = input()
    T = input()
    l = []
    N, M = len(S), len(T)
    for i in range(N-M+1):
        if all(T[j] == S[i+j] or S[i+j] == '?' for j in range(M)):
            w = S[:i]+T+S[i+M:]
            w = w.replace('?', 'a')
            l.append(w)
    if l:
        print(sorted(l)[0])
    else:
        print('UNRESTORABLE')


if __name__ == '__main__':
    main()