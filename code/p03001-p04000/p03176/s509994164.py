N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
size = 2**N.bit_length()
seg = [0 for i in range(2*size + 1)]

def update(i, x):
  i += size
  seg[i] = x
  while 1 < i:
    i >>= 1
    seg[i] = max(seg[i<<1|0], seg[i<<1|1])

def query_(a, b, k, l, r):
  ret = 0

  a += size
  b += size
  while a < b:
    if b & 1:
      b -= 1
      ret = max(ret, seg[b])

    if a & 1:
      ret = max(ret, seg[a])
      a += 1

    a >>= 1
    b >>= 1

  return ret


def query(a, b):
  return query_(a, b, 1, 0, N)

for i in range(N):
  temp = query(0, H[i])
  update(H[i], temp+A[i])

print(query(0, N+1))