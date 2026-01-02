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
    hs = LI()
    anss = [0 for i in range(n)]
    max_ = 0
    for i in range(n - 1):
        if hs[n - i - 1] <= hs[n - i - 2]:
            anss[n - i - 2] = anss[n - i - 1] + 1
            if anss[n - i - 2] > max_:
                max_ = anss[n - i - 2]

    print(max_)



if __name__ == '__main__':
    main()