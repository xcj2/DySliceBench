from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n = int(input())
    aa = LI()
    #どこかで2つに区切って、左の上位n項の和と右の下位n項の和を求め、その差を最大にすればいい
    # 左からn+i項のうち上位n項の和をmax_Lに記録
    max_L = [0] * (n + 1)
    hp = []
    s = 0
    for a in aa[:n]:
        heappush(hp, a)
        s += a
    max_L[0] = s
    for i, a in enumerate(aa[n:2 * n], 1):
        if a > hp[0]:
            s -= heappop(hp)
            s += a
            heappush(hp, a)
        max_L[i] = s

    # 右からn+i項のうち下位n項の和をmin_Rに記録
    min_R = [0] * (n + 1)
    hp = []
    s = 0
    for a in aa[:-n - 1:-1]:
        heappush(hp, -a)
        s += a
    min_R[n] = s
    for i, a in enumerate(aa[-n - 1:-2 * n - 1:-1]):
        if a > hp[0]:
            s -= -heappop(hp)
            s += a
            heappush(hp, -a)
        min_R[n - 1 - i] = s
    # print(max_L)
    # print(min_R)
    #各区切り方にのうち、左ー右が最大のものが答え
    print(max(s0 - s1 for s0, s1 in zip(max_L, min_R)))

main()
