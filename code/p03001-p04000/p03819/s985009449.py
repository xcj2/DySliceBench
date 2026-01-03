import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))


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
            i += i & -i

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


def main():
  n, m = map(int, input().split())
  lr = [tuple(map(int, input().split())) for _ in range(n)]
  bt = BIT(m)

  lr = list(sorted(lr, key=lambda x: x[1]-x[0]))
  i = 0
  for d in range(1, m+1):
    for i in range(i, n):
      if lr[i][1]-lr[i][0]+1==d:
        bt.add(lr[i][0], 1)
        bt.add(lr[i][1]+1, -1)
        if i == n-1:
          i = n
          break
      else:
        break

    ans = n - i
    for j in range(d, m+1, d):
      ans += bt.get(j)
    print(ans)


if __name__ == '__main__':
  main()
