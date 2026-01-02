# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template



def main():
    N = ii()
    S = li()
    S = list(map(int, S))
    res = [[N for i in range(10)]for j in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(10):
            res[i][j] = res[i + 1][j]
            res[i][S[i]] = i
    cnt = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                first = res[0][i]
                if(first != N):
                    second = res[first + 1][j]
                    if(second != N):
                        third = res[second + 1][k]
                        if(third != N):
                            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
