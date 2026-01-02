from collections import *
from heapq import *
import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def LcpByZ(target):
    len_t = len(target)
    lcp = [-1] * len_t
    top = 1  # 右の箱において、左の箱の0に対応する点
    left = 0  # 左の箱の左端(本当はここでので宣言は不要だけど理解の為)
    right = 0  # 左の箱の右端
    lcp[0] = 0
    while top < len_t:
        # 箱を右に広げていく
        while top + right < len_t and target[right] == target[top + right]:
            right += 1
        # 右の箱左端のlcpを記録
        lcp[top] = right
        left = 1
        # 箱の幅が0だったらtopを動かして、このターン終了
        if right == 0:
            top += 1
            continue
        # lcpを記録しながら箱を左に縮めていく（最初の条件重要）
        while left + lcp[left] < right and left < right:
            lcp[top + left] = lcp[left]
            left += 1
        # topを右の箱の左端にして、左の箱を0まで戻す
        top += left
        right -= left
        left = 0  # これも本当は不要
    return lcp

def main():
    n=II()
    s=SI()
    ans=0
    for i in range(n):
        lcp=LcpByZ(s[i:])
        for j in range(len(lcp)):
            if lcp[j]>ans and j>=lcp[j]:ans=lcp[j]
    print(ans)

main()
