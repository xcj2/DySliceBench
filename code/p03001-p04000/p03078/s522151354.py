# https://atcoder.jp/contests/abc123/tasks/abc123_d

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

X, Y, Z, K = MAP()
A = LIST()
B = LIST()
C = LIST()

# A.sort(reverse=True); B.sort(reverse=True); C.sort(reverse=True)

E = []
for a in A:
    for b in B:
        E.append(a+b)
E.sort(reverse=True)

ans = []

for c in C[:K]:
    for e in E[:K]:
        ans.append(c+e)
ans.sort(reverse=True)

for i, a in enumerate(ans):
    if i < K:
        print(a)
    else:
        break