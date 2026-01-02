def compute():
  from sys import stdin
  N, M = list(map(int, stdin.readline().split()))
  E = [tuple(map(lambda i: int(i) - 1,
                  stdin.readline().split())) for _ in range(M)]

  cnt = [1] * N
  par = [x for x in range(N)] # Disjoint set

  def parent(x):
    if par[x] == x:
      return x
    par[x] = parent(par[x])
    return par[x]

  def joinset(a,b):
    pa, pb = parent(a), parent(b)
    if pa==pb:
      return 0

    x, y = cnt[pa], cnt[pb]
    ret = x * y # decrement value

    # joining set
    if pb > pa:
      pa, pb = pb, pa
    cnt[pa], cnt[pb] = cnt[pa] + cnt[pb], 0
    par[pb] = pa

    return ret


  toprint = []
  cur = N * (N-1) // 2
  for a,b in reversed(E):
    toprint.append(cur)
    # print(cur, cnt, par, sep="\n")
    cur -= joinset(a,b)

  print(*reversed(toprint), sep="\n")


if __name__ == "__main__":
  compute()
