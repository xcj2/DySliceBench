import sys

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    ds = LI()
    ans = 0
    c = 0
    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            ans += ds[i] * ds[j]
            c += 1
    assert c == n*(n-1)/2
    print(ans)

if __name__ == '__main__':
    main()