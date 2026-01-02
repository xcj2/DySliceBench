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
    flag = True
    if N % 2 == 1:
        exit("No")
    for i in range(N // 2):
        if S[i] != S[i + N // 2]:
            flag = False
    if flag:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    main()
