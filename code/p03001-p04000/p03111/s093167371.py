import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B, C = mapint()
Ls = [int(input()) for _ in range(N)]
ans = 10**18
def dfs(a, b, c, idx, magic):
    global ans
    if idx==N:
        if a==0 or b==0 or c==0:
            return
        magic -= 30
        magic += abs(A-a)
        magic += abs(B-b)
        magic += abs(C-c)
        ans = min(ans, magic)
        return
    nx = Ls[idx]
    dfs(a+nx, b, c, idx+1, magic+10)
    dfs(a, b+nx, c, idx+1, magic+10)
    dfs(a, b, c+nx, idx+1, magic+10)
    dfs(a, b, c, idx+1, magic)

dfs(0, 0, 0, 0, 0)
print(ans)
