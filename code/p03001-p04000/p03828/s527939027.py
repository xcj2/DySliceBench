from functools import reduce
N = int(input())
g = 10 ** 9 + 7

def add(a, b):
  return (a + b) % g
def mul(a, b):
  return (a * b) % g

def adda(a, p1, p2):
    for x in range(len(a)):
        a[x] = add(p1[x], p2[x])

d = []
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
for i in range(2, N+1):
  for j in (x for x in d if x * x <= N):
    if i % j == 0:
      adda(DP[i], DP[j], DP[i//j])
      break
  else:
    d.append(i)
    DP[i][i] = 1
  adda(ans, ans, DP[i])

print(reduce(mul, [x + 1 for x in ans[1:N+1]]))
