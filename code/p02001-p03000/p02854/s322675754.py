def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7


n = INT()
l = MAP()

s = sum(l)
tmp=0
for i in range(n):
    tmp+=l[i]
    if tmp >= s/2:
        p1 = tmp - (s/2)
        idx1 = i
        break

tmp=0
for i in range(n-1,-1,-1):
    tmp+=l[i]
    if tmp >= s/2:
        p2 = tmp - (s/2)
        idx2 = i
        break

if p1 <= p2:
    left = sum(l[:idx1+1])
    right = sum(l[idx1+1:])
else:
    left = sum(l[:idx2])
    right = sum(l[idx2:])
print(abs(right-left))