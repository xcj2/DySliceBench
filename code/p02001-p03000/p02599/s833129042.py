import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, Q = mapint()
Cs = list(mapint())
LR = []
for i in range(Q):
    l, r = mapint()
    k = r*(10**12)+l*(10**6)+i
    LR.append(k)
LR.sort()
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
i = 0
last_appeared = [-1]*(N+1)
for k in LR:
    ans_idx = k%(10**6)
    l = k//(10**6)%(10**6)
    r = k//(10**12)
    while i<r:
        c = Cs[i]
        if last_appeared[c]==-1:
            last_appeared[c] = i+1
            add(A, i+1, 1)
        else:
            past = last_appeared[c]
            last_appeared[c] = i+1
            add(A, past, -1)
            add(A, i+1, 1)
        i += 1
    ans[ans_idx] = sums(A, r)-sums(A, l-1)
for a in ans:
    print(a)