from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
b = inpl()
dif = sum(a) - sum(b)
if dif < 0:
    print(-1)
else:
    m_cnt = 0
    m_num = 0
    p = []
    for i in range(n):
        if a[i] - b[i] > 0:
            p.append(a[i] - b[i])
        elif a[i] - b[i] < 0:
            m_cnt += 1
            m_num += b[i] - a[i]
    cnt = 0
    p.sort()
    while m_num > 0:
        cnt += 1
        tmp = p.pop()
        m_num -= tmp
    print(m_cnt + cnt)