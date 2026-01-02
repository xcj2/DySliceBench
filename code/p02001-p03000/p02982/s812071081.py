import bisect

N, D = map(int, input().split())
Xss = []
for i in range(N):
    Xss.append(list(map(int, input().split())))

def distance2(p1, p2):
    ddt = 0
    for i in range(D):
        r = (p1[i] - p2[i])
        ddt += (r * r)

    return ddt

class SquareRoot(object):
    def __init__(self, n):
        self.n = n
    def __getitem__(self, index):
        return index * index
    def __len__(self):
        return self.n

def try_square_root(n2):
    n = bisect.bisect_left(SquareRoot(n2), n2)
    return n if n*n == n2 else None

result = []
lss = len(Xss)
r = 0
for i in range(lss):
  for j in range(i + 1, lss):
      p1 = Xss[i]
      p2 = Xss[j]
      d = distance2(p1, p2)
      if try_square_root(d) is not None:
          r += 1
print(r)
