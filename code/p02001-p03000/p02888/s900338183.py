import sys
import bisect

sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]

def main():
    n = II()
    ls = LI()
    ls = sorted(ls)
    ans = 0
    for i in range(n):
        for j in range(i):
            ans += j - (bisect.bisect_right(ls[:j], ls[i] - ls[j]))

            # ans += a
            # print(ls[i], ls[j], bisect.bisect_left(ls[:j], ls[i] - ls[j]))
            # if ls[i] < ls[j] + ls[h]:
            #     # print(ls[i], ls[j], ls[h])

    print(ans)

if __name__ == '__main__':
    main()