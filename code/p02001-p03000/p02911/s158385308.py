import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n, k, q = LI()
    ans = [0 for i in range(n)]
    for i in range(q):
        a = II()
        ans[a-1] += 1
    for i, v in enumerate(ans):
        if k > (q - v):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()