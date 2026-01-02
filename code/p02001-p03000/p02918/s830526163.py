import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def perr(s): return print(s, file=sys.stderr)
N, K = LI()
S = input()

"""

答えは0以上N-1以下になる
まず何回ひっくり返せるかが重要
N==Kなら、全部ひっくり返して最大値となる
K==N-1なら、最大値から1箇所は矛盾する
LLRRLLなら
LLはRRになる
愚直回は、毎回どの区間をひっくり返すかを探索する
そうすると、区間の選び方だけでもかなり多い
好きな回数だけ選ぶと
まず塊の場所を特定する
6 1
LRLRRL
なら
てかどちらに統一するか問題もある
RRを
一番つながってるやつをひっくり返すのでいいか
Lにする場合とRにする場合を分けて考える
上のやつなら
Lにする場合
RRを返して
LRLLLL
で3
Rにする場合
LRRRRLになって3となる

9 2
RRRLRLRLL
の場合
Lの場合
LLLLRLRLL
になり、
LLLLLLRLL
5
Rの場合
111110101
111111101

長さをリストにすると
3, 1, 1, 1, 1, 2
最大にすると
5, 1, 1, 1, 1
6, 1, 1, 1

3, 1, 1, 1, 1, 2
3 1 1 4
7 1 1
RRRLRLLLL
LRLLLLLLL
だと6
RRRRRLRLL
RRRRRRRLR

LRLLLLRLL
LRLLLLLLL

RRRRLRRLL
RRRRRRLLR

RRRLLRLLL
RRRRRRLRR

RRRRRLRLR
RRRRRRLRR

-- RRRLRLRLL

RRRLRRRLR
LLLLRRRRR


長さをリストにすると
3, 1, 1, 1, 1, 2
3 3 1 2
3 6
2 + 5

RRRLLLRLL
RRRLLLLLL

まず、リストを作成

3 1 1 4
3 3 1 2
RRR LLL R LL
3 6
2 + 5
または


5 1 1 1


5 3
4 + 2

最小値の組み合わせをあわせる？
2個ずつ減っていく

LRLRRL
の場合
1 1 1 2 1
3 2 1
2+1 = 3
1 1 4 = 3

3 2 1
6
何回裏返せるかで決まってる

塊の数が
6子なら
6
4
26子なら
6
4
26子なら
6
4
26子なら
6
4
26子なら
6
4
26子なら
6
4
2
というふうに減っていく
4塊の場合はもう決まってる
3 3 1 2 = 5
3 1 1 4 = 5

-- RRRLRLRLL
3 1 1 1 1 2
6塊
まず9-6
ほんで3あまってる
答えは必ず3

"""
tmp = 1
l = []
for i in range(N-1):
    if S[i] == S[i+1]:
        if i == N - 2:
            tmp += 1
            l.append(tmp)
        else:
            tmp += 1
    else:
        if i == N - 2:
            l.append(tmp)
            l.append(1)
        else:
            l.append(tmp)
            tmp = 1
#  print(l)

len_l = len(l)
len_l -= 2 * K
if len_l <= 1:
    print(N - 1)
    exit()
elif len_l <= 2:
    print(N - 2)
else:
    ans = N - len_l
    print(ans)

