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


test_str = '''
2
100 1 1
1 100
'''


def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()
  al = IN_L_I()
  bl = IN_L_I()

  killed = 0
  for i, b in enumerate(bl):
    a1 = al[i] - b
    if a1 >= 0:
      killed += b
      continue

    killed += al[i]

    b = b - al[i]
    a2 = al[i + 1] - b
    if a2 < 0:
      killed += al[i + 1]
      al[i + 1] = 0
    else:
      killed += b
      al[i + 1] -= b

  print(killed)
  return None


def B():
  return None


def C():
  return None


MAIN()
