import sys
from itertools import product

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    ps = [[] for i in range(n)]
    # eva = [[] for i in range(n)]
    for i in range(n):
        a = II()
        for j in range(a):
            ps[i].append(LI())
    max_ = 0
    for c in product([0, 1], repeat=n):
        c = list(c)
        # print(c)
        for i, p in enumerate(c):
            if p == 1:
                for opp in ps[i]:
                    # print(c[opp[0] - 1], opp[1])
                    if c[opp[0] - 1] != opp[1]:
                        # print(c[opp[0] - 1], opp[1])
                        break
                else:
                    continue
                break
        else:
            # print(c)
            max_ = max(max_, sum(c))
    print(max_)

if __name__ == '__main__':
    main()