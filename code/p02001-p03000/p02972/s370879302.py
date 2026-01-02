import sys
sys.setrecursionlimit(10**7)
import math
mod = 10**9 + 7
def I(): return int(input())
def II(): return map(int, input().split())
def L(): return list(map(int, input().split()))
def TWO(M):
  L=[0]*M
  R=[0]*M
  for i in range(M):
    L[i],R[i] = II()
  return L, R
N = I()
a = L()
ans = [-1]*(N)
for i in range(N)[::-1]:
  temp = N//(i+1)
  x = []
  for j in range(2,temp+1):
    x.append(ans[(i+1)*j-1])
  ans[i] = abs(a[i]-sum(x)%2)
  #print(i+1, x, ans)

print(ans.count(1))
ans_tmp = []
for i in range(N):
  if ans[i]==1:
    ans_tmp.append(i+1)
print(*ans_tmp)