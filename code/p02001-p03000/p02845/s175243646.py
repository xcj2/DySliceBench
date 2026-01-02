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
    color = [-1] * 3
    n = ii()
    A = lmi()
    num = [0] * (max(A) + 10)
    ans = 1
    num[0] = 3
    for i in range(n):
        num[A[i] + 1] += 1
        ans *= num[A[i]]
        num[A[i]] -= 1
        ans %= 1000000007
    print(ans)


if __name__ == '__main__':
    main()
