import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, Q = mapint()
Cs = list(mapint())
LR = []
for i in range(Q):
    l, r = mapint()
    LR.append((l, r, i))
LR.sort(key=lambda x:x[1])
A = [0]*N

def add(A,a,w):#リストに値を追加する関数
    x = a
    while x <= N:
        A[x-1] += w
        x += x&(-x)

def sums(A,a):#k番目までの和
    x = a
    S = 0
    while x != 0:
        S += A[x-1]
        x -= x&(-x)
    return S

ans = [0]*Q
idx = 0
dic = {}
for i in range(N):
    c = Cs[i]
    if c not in dic:
        dic[c] = i+1
        add(A, i+1, 1)
    else:
        past = dic[c]
        dic[c] = i+1
        add(A, past, -1)
        add(A, i+1, 1)
    while idx<Q and LR[idx][1]<=i+1:
        l, r, ans_idx = LR[idx]
        ans[ans_idx] = sums(A, r)-sums(A, l-1)
        idx += 1
for a in ans:
    print(a)