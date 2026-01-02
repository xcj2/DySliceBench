import sys
input = sys.stdin.readline

MOD = 998244353

class BIT:
  def __init__(self, n):
    self.size = n
    self.tree = [0 for _ in range(n+1)]
    self.p = 2**(n.bit_length() - 1)
    self.dep = n.bit_length()

  def get(self, i):
    s = 0
    while i > 0:
      s += self.tree[i]
      i -= i & -i
    return s

  def add(self, i, x):
    while i <= self.size:
      self.tree[i] += x
      i += (i & -i)

  def bl(self, v):
    if v <= 0:
      return -1
    s = 0
    k = self.p
    for _ in range(self.dep):
      if s + k <= self.size and self.tree[s+k] < v:
        s += k
        v -= self.tree[s+k]
      k //= 2
    return s + 1


def compress(L):
  L2 = list(set(L))
  L2.sort()
  C = {v: k for k, v in enumerate(L2, 1)}
  return L2, C


def main():
  n = int(input())
  ans = n * pow(2, n-1, MOD) % MOD
  xy = []
  for _ in range(n):
    xy.append(tuple(map(int, input().split())))
  xy.sort()
  py = [_xy[1] for _xy in xy]
  _, Cy = compress(py)
  py = [Cy[p] for p in py]
  BIT1 = BIT(n)

  for i in range(n):
    y = py[i]  # 注目する点
    c = BIT1.get(y)  # 左下
    d = y - c - 1  # 右下
    a = i - c  # 左上
    b = n - 1 - a - c - d  # 右上
    a2 = pow(2, a, MOD)
    b2 = pow(2, b, MOD)
    c2 = pow(2, c, MOD)
    d2 = pow(2, d, MOD)
    ans += (a2-1) * b2 * c2 * (d2-1)  # 絶対に左上右下は含む
    ans += a2 * (b2-1) * (c2-1) * d2  # 絶対に右上左下は含む
    ans -= (a2-1) * (b2-1) * (c2-1) * (d2-1)  # 数えすぎ
    ans %= MOD
    BIT1.add(y, 1)

  print(ans)


if __name__ == '__main__':
  main()