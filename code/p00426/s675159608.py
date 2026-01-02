INF = 10 ** 20

full_move1_memo = [None] * 16
full_move2_memo = [None] * 16

def full_move1(n):
  if n == 1:
    return 2
  if full_move1_memo[n]:
    return full_move1_memo[n]
  a = full_move1(n - 1) * 3 + 2
  full_move1_memo[n] = a
  return a

def full_move2(n):
  if n == 1:
    return 2
  if full_move2_memo[n]:
    return full_move2_memo[n]
  a = full_move1(n - 1) * 2 + 2
  full_move2_memo[n] = a
  return a

def half_move(n):
  if n == 1:
    return 1
  if full_move1_memo[n - 1]:
    return full_move1_memo[n - 1] + 1
  return full_move1(n - 1) + 1

def solve():
  while True:
    n, m = map(int, input().split())
    if not n:
      break

    lst = [list(map(int,input().split()))[1:] for _ in range(3)]
    inds = [-1 for i in range(n)]

    for i in range(3):
      for j in lst[i]:
        inds[j - 1] = i
    
    ans = INF
    for p in [0, 2]:
      rec = 0
      for i in range(n):
        pi = inds[i]
        if abs(pi - p) == 2:
          rec += full_move2(n - i)
        elif abs(pi - p) == 1:
          rec += half_move(n - i)
          p = (p + 2) % 4
      if rec < ans:
        ans = rec

    if ans <= m:
      print(ans)
    else:
      print(-1)

solve()
