import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    A, B = MI()
    x = 10 * B
    for i in range(x, x + 10):
        y = int(i * 8 / 100)
        if y == A:
            print(i)
            exit()
    print(-1)
if __name__ == "__main__":
    main()
