N, M, K = map(int, input().split())
 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
def solve(A, N, B, M, K):
  
  def cumsum(l):
    rt = [0]
    s = 0
    for n in l:
      s += n
      rt.append(s)
    return rt
  
  preA = cumsum(A)
  preB = cumsum(B)
  
  s, e = 0, N + M
  
  def can_read(num):
    for i in range(N + 1):
      j = num - i
      if j >= 0 and j < (M + 1) and (preA[i] + preB[j]) <= K:
      	return True
    return False

  res = 0
  while s <= e:
    mid = s + (e - s) // 2
    can = can_read(mid)
    
    if can:
      res = mid
      s = mid + 1
    else:
      e = mid - 1
  
  return res

res = solve(A, N, B, M, K)

print(res)