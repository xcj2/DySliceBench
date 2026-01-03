def main():
  n, m = map(int, input().split())
  lr = [tuple(map(int, input().split())) for _ in range(n)]
  BIT = [0 for _ in range(m+1)]

  def bit_add(a, w):
    x = a
    while x <= m:
      BIT[x] += w
      x += x&-x

  def bit_sum(a):
    ret = 0
    x = a
    while x > 0:
      ret += BIT[x]
      x -= x&-x
    return ret

  lr = list(sorted(lr, key=lambda x: x[1]-x[0]))
  i = 1
  for d in range(1, m+1):
    while i<=n and lr[i-1][1]-lr[i-1][0]+1==d:
      bit_add(lr[i-1][0], 1)
      bit_add(lr[i-1][1]+1, -1)
      i += 1
    ans = n - i + 1
    for j in range(d, m+1, d):
      ans += bit_sum(j)
    print(ans)


if __name__ == '__main__':
  main()
