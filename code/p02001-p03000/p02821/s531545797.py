def nibutan(n, M):
  ok = 0
  ng = M + 1
  while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    #print("value:", mid)
    if nasu(mid) >= n:
      ok = mid
    else:
      ng = mid
  return ok

def nasu(x):
  ans = 0
  for i in A:
    #print("L:", i, end = " ")
    t = N - hogetan(x - i)
    #print("n:", t)
    ans += t
  return ans

def hogetan(n):
  ok = N
  ng = -1
  while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if A[mid] >= n:
      ok = mid
    else:
      ng = mid
  return ok

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))


A.sort()
MAX = A[-1] + A[-1]
inf = MAX + 10

t = nibutan(M, MAX)
mi = inf
cnt = 0
ans = 0
for i in A:
  k = hogetan(t - i)
  n = N - k
  cnt += n
  if n != 0:
    mi = min(mi, i + A[k])
  ans += n * 2 * i

ans -= mi * (cnt - M)

print(ans)