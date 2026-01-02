import io
import sys


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


def make_divisors(n):
  divisors = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)

  # divisors.sort()
  return divisors


test_str = '''
4
1 0 1 0
'''
#
# 1 1 1

def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()
  li = IN_L_I()

  tmp = [False] * n
  tmp2 = [False] * n
  for i, b in enumerate(reversed(li)):
    ci = n - i - 1
    # print("hoge:",i,b,ci)
    if b == 1 and not tmp[ci]:
      tmp[ci] = True
      tmp2[ci] = True

    if b == 0 and tmp[ci]:
      tmp[ci] = False
      tmp2[ci] = True

    if tmp2[ci]:
      # print(ci, " || ",make_divisors(ci + 1))
      for j in make_divisors(ci + 1):
        if j != ci + 1:
          tmp[j - 1] = not tmp[j - 1]

    # print(tmp)
    # print(tmp2)

  puts = [i for i, x in enumerate(tmp2) if x]
  print(len(puts))
  if len(puts) > 0:
    print(" ".join([str(i + 1) for i in puts]))
  return None


def B():
  return None


def C():
  return None


MAIN()
