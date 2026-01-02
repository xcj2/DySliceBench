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
    n = II()
    c = defaultdict(int)
    for i in range(n):
        c["".join(sorted(S()))] += 1
    ans = 0
    for k, v in c.items():
        ans += int(v * (v - 1) /2)
    print(ans)
if __name__ == '__main__':
    main()