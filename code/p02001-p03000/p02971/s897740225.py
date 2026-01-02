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
5
5
'''


def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()
  l = []
  for i in range(0, n):
    l.append(IN_I())

  l2 = l.copy()
  l.sort()

  for i in l2:
    if i == l[-1]:
      print(l[-2])
    else:
      print(l[-1])

  return None


def B():
  return None


def C():
  return None


MAIN()
