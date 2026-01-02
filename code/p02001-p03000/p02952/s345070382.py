import io
import sys

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
136
'''


def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()

  t = 0
  if n > 9:
    t += 9

  if n > 999:
    t += 900

  if n > 99999:
    t += 90000

  if n <= 9:
    t += n
  elif 99 < n <= 999:
    t += n - 99
  elif 9999 < n <= 99999:
    t += n - 9999

  print(t)
  return None


def B():
  return None


def C():
  return None


MAIN()
