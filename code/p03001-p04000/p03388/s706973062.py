def is_ok(x,n):
  if x**2<=n:
    return True
  else:
    return False

def meguru_bisect(ng, ok,n):
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid,n):
      ok = mid
    else:
      ng = mid
  return ok

def sqrt(n):
  return meguru_bisect(n,1,n)

Q = int(input())
for _ in range(Q):
  A,B  = list(map(int,input().split()))
  score = A*B-1
  maxA = score//(B+1)
  maxB = score//(A+1)
  crit = sqrt(score)
  ans = 0
  if maxA:
    if crit<maxA:
      ans += crit+(score//(crit+1)-score//maxA)+1
    else:
      ans += maxA
  if maxB:
    if crit<maxB:
      ans += crit+(score//(crit+1)-score//maxB)+1
    else:
      ans += maxB
  print(ans)