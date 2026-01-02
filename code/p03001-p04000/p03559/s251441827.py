n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

def isOK(target,mid):
  return target < mid
def isOK_dep(target,mid):
  return target <= mid

def bin_search(l,r,li,target):
  left = l
  right = r
  while right-left>1:
    mid = (left + right)//2
    if isOK(target,li[mid]):
      right = mid
    else:
      left = mid
  return left

def bin_search_dep(l,r,li,target):
  left = l
  right = r
  while right-left>1:
    mid = (left + right)//2
    if isOK_dep(target,li[mid]):
      right = mid
    else:
      left = mid
  return left

ans = 0
for i in range(n):
  top,bottom = 0,0
  top += bin_search_dep(-1,n,A,B[i]) + 1
  bottom += n-bin_search(-1,n,C,B[i])-1
  ans += top * bottom
print(ans)