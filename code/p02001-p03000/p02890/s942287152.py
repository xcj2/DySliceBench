N = int(input())
A = list(map(int, input().split()))

A.sort()
D = [1]
t = A[0]
for i in range(1, N):
  if A[i] == t:
    D[-1] += 1
  else:
    D.append(1)
    t = A[i]

D.sort()
L = len(D)
S = [0] * L
S[0] = D[0]
for i in range(1, L):
  S[i] = S[i - 1] + D[i]

def hersCode(n):
  ok = 0
  ng = N + 1
  while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if nasu(mid, n):
      ok = mid
    else:
      ng = mid
  return ok

def honya(n):
  ok = -1
  ng = L
  while abs(ok - ng) > 1:
    mid = abs(ok + ng) // 2
    if D[mid] >= n:
      ok = mid
    else:
      ng = mid
  return ok + 1

def nasu(x, n):
  a = honya(x)
  ans = a * x + S[L - a - 1]
  if ans >= n * x:
    return True
  else:
    return False

D.sort(reverse = True)
for i in range(1, N + 1):
  if L < i:
    print(0)
    continue
  print(hersCode(i))