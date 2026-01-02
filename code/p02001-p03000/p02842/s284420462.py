import sys
import math

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    ans = int(math.floor(n / 1.08))

    if math.floor(ans * 1.08) == n:
        print(ans)
    elif math.floor((ans + 1) * 1.08) == n:
        print(ans + 1)
    else:
        print(":(")

if __name__ == '__main__':
    main()