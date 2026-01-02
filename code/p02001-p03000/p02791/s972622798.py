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
    ps= LI()
    mins = []
    min_ = 10000000
    for i, v in enumerate(ps):
        if min_ > v:
            mins.append(v)
            min_ = v
        else:
            mins.append(min_)
    count = 0
    for i in range(n):
        if mins[i] >= ps[i]:
            count += 1
    print(count)


if __name__ == '__main__':
    main()