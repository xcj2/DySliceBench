#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

"""
URL: https://atcoder.jp/contests/dp/tasks/dp_l
L - Deque / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 
100 点

問題文
太郎君と次郎君が次のゲームで勝負します。
最初に、数列 a=(a1,a2,…,aN) が与えられます。 
a が空になるまで、二人は次の操作を交互に行います。 
先手は太郎君です。a の先頭要素または末尾要素を取り除く。 
取り除いた要素を x とすると、操作を行った人は x 点を得る。
ゲーム終了時の太郎君の総得点を X、次郎君の総得点を Y とします。 
太郎君は X−Y を最大化しようとし、次郎君は X−Y を最小化しようとします。

二人が最適に行動すると仮定したとき、X−Y を求めてください。

解説:
ただの区間DP
しかし、Pythonはカスなので工夫が必要
知見
    ====================================================================
    |dp[i][j]に-dp[i][j-1] or -dp[i+1][j]の加算結果を与えれば             |
    |    右辺の式はすべて符号反転するので－側の最小を目指すというのと         |
    |        ＋の最大を目指すというのを満たすのでその区間における            |
    |           プレイヤーの最善スコアが出る                               |
    ====================================================================|

"""

#solve
def solve():
    n = II()
    a = LI()
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n - 2, -1, -1):
        dpi = dp[i]
        dpi1 = dp[i + 1]
        ai = a[i]
        for j in range(i + 1, n):
            dpi[j] = max(ai-dpi1[j], a[j]-dpi[j-1])
    print(dp[0][n - 1])
    return


#main
if __name__ == '__main__':
    solve()
