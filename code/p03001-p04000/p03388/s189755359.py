#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    s = S()
    s.sort()
    if s == ["a", "b", "c"]:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    a, b, k = LI()
    ans = []
    for i in range(a, min(a + k, b + 1)):
        ans.append(i)
    for i in range(max(b - k + 1, a + k), b + 1):
        ans.append(i)
    for i in ans:
        print(i)
    return

#C
def C():
    abc= LI()
    abc.sort()
    a,b,c = abc
    a1 = (c - a) % 2
    b1 = (c - b) % 2
    if a1 and b1:
        print((c - a) // 2 + (c - b) // 2 + 1)
        return
    if a1 or b1:
        print((c - a) // 2 + (c - b) // 2 + 2)
        return
    print((c - a) // 2 + (c - b) // 2 )

    return

# D
# 解説AC

# a <= b として一般性を失わない
# 1: a = b のとき
# (a-k)*(a+k) = a*a - k*k < a*a
# であることを考えると0<k<aのすべてをとれて、
# 1回目にa-k,2回目にa+kもしくは2回目にa-k,1回目にa+kをとっている場合
# 満たすことがわかるこれは2*a-2人である
# ここでa*a > n*k を考えるとn,kどちらかはa-1以下である
# また、a+1以上である場合、もう一方がa-1以下であることが確定するため
# 片方がa+1以上である場合の個数はもう一方がa-1以下である場合に数えている 
# よって個数の上限が2*a-2人であるためこれが解であることがわかる
# 
# 2: c*c < a*b かつ c*(c+1) >= a*b を満たすcを考えるとき
# 1回目,2回目どちらかはc以下をとる必要があるゆえに上と同様に考えれば
# (c-k)*(c+k)を考えると0<=k<=c-1を考えればよくk=0で同じ組になることから
# 2*c-1人に見えるがc-k = aとなるときは除去しなければならないため
# 2*c-2人が解になる
# 
# 3: c*c < a*b かつ c*(c+1) < a*b を満たす最大のcを考えるとき
# 2と同様に(c-k)*(c+k)を考えるのではなく(c-k)*(c+1+k)の組として
# 考えればよく0<=k<c-1を考えてよく2*c人に見えるが、c-k=aのときだけ
# 除外する必要があるので2*c-1人が解になる 
def D():
    for _ in range(II()):
        a, b = LI()
        c = math.ceil(math.sqrt(a * b)) - 1
        print(2 * a - 2 if a == b else 2 * c - 1 - (c * (c + 1) >= a * b))
    return

#Solve
if __name__ == '__main__':
    D()
