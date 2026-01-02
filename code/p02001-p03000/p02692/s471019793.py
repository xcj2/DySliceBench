import random
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n,a,b,c = get_nums_l()
d = {
    "A": a,
    "B": b,
    "C": c
}
S = []
for _ in range(n):
    S.append(input())

def dfs(i, x, history):

    if d[S[i][1-x]] == 0:
        return False

    d[S[i][x]] += 1
    d[S[i][1-x]] -= 1

    history.append(S[i][x])

    if i == n-1:
        return True

    nex = random.randint(0, 1)

    ok = dfs(i+1, nex, history)
    if ok:
        return ok

    ok = dfs(i+1, 1-nex, history)

    if ok:
        return ok

    # バックトラック
    history.pop()
    d[S[i][x]] -= 1
    d[S[i][1-x]] += 1

    return False

history = deque()
ok = dfs(0, 0, history) or dfs(0, 1, history)

print("Yes" if ok else "No")
if ok:
    for s in history:
        print(s)
