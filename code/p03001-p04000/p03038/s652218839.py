import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

import heapq

def solve():
    n, m = MI()
    A = LI()
    hp = []
    memo = {}
    for a in A:
        if memo.get(a, 0) == 0:
            hp.append(-a)
            memo[a] = 1
        else:
            memo[a] += 1
    # print(memo)
    heapq.heapify(hp)

    for i in range(m):
        b, c = MI()
        if memo.get(c, 0) == 0:
                heapq.heappush(hp, -c)
                memo[c] = b
        else:
            memo[c] += b

    # print(memo)
    ans = 0
    left = n
    while left > 0:
        val = - heapq.heappop(hp)
        t = memo[val]
        # print(val, t)
        ans += val * min(t, left)
        left -= t
    print(ans)


if __name__ == '__main__':
    solve()
