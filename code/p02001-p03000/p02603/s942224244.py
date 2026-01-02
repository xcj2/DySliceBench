import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

memo = {}
s = set()

ans = 0
def dfs(idx, money, stocks):
    global ans
    if idx==N:
        ans = max(ans, money)
        return
    a = As[idx]
    if (idx, stocks) in s:
        if money<=memo[(idx, stocks)]:
            return
    s.add((idx, stocks))
    memo[(idx, stocks)] = money
    dfs(idx+1, money+stocks*a, 0)
    dfs(idx+1, money, stocks)
    cnt = money//a
    dfs(idx+1, money-cnt*a, stocks+cnt)

dfs(0, 1000, 0)
print(ans)