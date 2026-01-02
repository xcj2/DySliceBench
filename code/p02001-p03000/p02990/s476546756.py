import io
import sys

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7


def IN_S():
  return input()


def IN_I():
  return int(input())


def IN_L_I():
  return list(map(int, input().split()))


def IN_L_S():
  return list(map(str, input().split()))


def STR_SPLIT(s, n):
  for l in range(0, len(s), n):
    yield s[0 + l:n + l]


def T_IN():
  global test_str
  sys.stdin = io.StringIO(test_str[1:-1])


test_str = '''
2000 3
'''


def MAIN():
  # T_IN()
  cmb_init(MOD)
  A()


def A():
  x = IN_L_I()
  n = x[0]
  k = x[1]

  res = []
  for i in range(1, k + 1):
    blue = f(k, i)

    # red = 0
    # red += f(n - k, i - 1)
    # red += f(n - k, i)
    # red += f(n - k, i)
    # red += f(n - k, i + 1)
    red = f2(n - k - (i - 1), i + 1)

    res.append((blue * red) % MOD)

  [print(i) for i in res]
  return None


def f(x: int, y: int):
  if x < y:
    return 0
  if x == y == 0:
    return 1
  if y < 1:
    return 0
  return f2(x - y, y)


def f2(x: int, y: int):
  return c(x + y - 1, y - 1)


def c(a: int, b: int):
  return cmb(a, b, MOD)


def track(func):
  def tracked(*args, **kwargs):
    result = func(*args, **kwargs)
    name = func.__name__
    arg_str = ",".join(repr(arg) for arg in args)
    print("%s(%s) -> %r" % (name, arg_str, result))
    return result

  return tracked


### CMB ###############################
def cmb(n, r, mod):
  if (r < 0 or r > n):
    return 0
  r = min(r, n - r)
  return g1[n] * g2[r] * g2[n - r] % mod


def cmb_init(mod):
  for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


N = 10 ** 4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

### CMB ###############################


MAIN()
