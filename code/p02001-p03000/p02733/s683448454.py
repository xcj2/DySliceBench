import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
H, W, K = MI()
S_ = [[] for _ in range(W)]
for i in range(H):
    s = S()
    for j in range(len(s)):
        S_[j].append(int(s[j]))



A = []
for i in range(2 ** (H - 1)):
    A_bit = []
    for j in range(H - 1):
        # 二進数表記でj回右にシフトして0桁目（一番下の桁）が1であればTrue
        if ((i >> j) & 1):
            A_bit.append(j)
    A.append(A_bit)


Ans_list = []
for a in A:
    sums = [0] * (len(a) + 1)
    ele = [0] * (len(a) + 1)
    ans = 0
    for s_ in S_:
        queue = deque(a)
        if queue == deque([]):
            ele[0] = sum(s_)
            if ele[0] > K:
                ans = 10 ** 6
                break
            sums[0] += sum(s_)
        else:
            x = queue.popleft()
            ele[0] = sum(s_[0:x + 1])
            if ele[0] > K:
                ans = 10 ** 6
                break
            sums[0] += sum(s_[0:x + 1])
            j = 1
            while queue != deque([]):
                y = queue.popleft()
                ele[j] = sum(s_[x + 1:y + 1])
                if ele[j] > K:
                    ans = 10 ** 6
                    break
                sums[j] += sum(s_[x + 1:y + 1])
                x = y
                j += 1
            ele[len(a)] = sum(s_[x + 1:H])
            if ele[len(a)] > K:
                ans = 10 ** 6
                break
            sums[len(a)] += sum(s_[x + 1:H])
        if max(sums) > K:
            ans += 1
            for k in range(len(a) + 1):
                sums[k] = ele[k]
    ans += len(a)
    Ans_list.append(ans)

print(min(Ans_list))