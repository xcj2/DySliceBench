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
14
99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1
'''

def MAIN():
  # T_IN()
  A()


def A():
  num = IN_I()
  lists = IN_L_I()
  lists.sort()

  print(lists[num // 2] - lists[num // 2 - 1])
  return None


def B():
  return None


def C():
  return None


MAIN()
