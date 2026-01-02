n = int(input())
a = list(map(int,input().split()))
ruiseki = [0]*(n+1)

for i in range(1,n+1):
  ruiseki[i] = a[i-1] + ruiseki[i-1]

#右側が大きいときにTrueを返す。
def judge(begin,mid,end):
  if ruiseki[mid]-ruiseki[begin] < ruiseki[end]-ruiseki[mid]:
    return True
  else:
    return False

def solvediff(begin,mid,end):
  return abs( ruiseki[mid]-ruiseki[begin] - (ruiseki[end]-ruiseki[mid]) )

def solve_num1(begin,mid,end):
  return abs( ruiseki[mid]-ruiseki[begin] )

def solve_num2(begin,mid,end):
  return abs( ruiseki[end]-ruiseki[mid] )


ans = float("inf")
for i in range(2,n-1):
  
  #PQの探索
  ok = i
  ng = 0
  min_num = float("inf")
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if judge(0,mid,i):
      ng = mid
    else:
      ok = mid
    if min_num > solvediff(0,mid,i):
      min_num = solvediff(0,mid,i)
      num1 = solve_num1(0,mid,i)
      num2 = solve_num2(0,mid,i)
  
  #RSの探索
  ok = n
  ng = i
  min_num = float("inf")
  while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if judge(i,mid,n):
      ng = mid
    else:
      ok = mid
    if min_num > solvediff(i,mid,n):
      min_num = solvediff(i,mid,n)
      num3 = solve_num1(i,mid,n)
      num4 = solve_num2(i,mid,n)
      
  ans = min(ans, max(num1,num2,num3,num4) - min(num1,num2,num3,num4))
  
print(ans)