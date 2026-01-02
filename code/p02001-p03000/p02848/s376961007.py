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
    cap = [chr(i) for i in range(65, 65 + 26)]
    N = ii()
    S = li()
    T = ['' for i in range(len(S))]
    for i in range(len(S)):
        T[i] = cap[(ord(S[i]) + 13 + N) % 26]
    print(''.join(T))
    return


if __name__ == '__main__':
    main()
