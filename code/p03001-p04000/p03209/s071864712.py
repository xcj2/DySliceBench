import sys
import heapq
from functools import lru_cache
sys.setrecursionlimit(10000)

# \n
def input():
    return sys.stdin.readline().rstrip()


def level(n, k):
    number = 2 ** (n + 1) - 3  # 一個レベル下のやつの数
    cn = 2**(n+2) -3
    if n == 0:
        return 1
    elif k==cn:
        return (2**(n+1) -1)

    else:
        if k == 1:
            return 0
        elif k <= 1 + number:
            return level(n - 1, k - 1)
        elif k == 2 + number:
            return level(n - 1, number) + 1
        else:
            return 1 + level(n - 1, number) + level(n - 1, min(number, k - number - 2))



def main():

    n,k=map(int,input().split())
    print(level(n,k))


if __name__ == "__main__":
    main()
