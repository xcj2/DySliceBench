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
3
500 300 200
'''


def MAIN():
  # T_IN()
  A()


def A():
  n = IN_I()
  nums = IN_L_I()
  nums.sort()
  t = nums.pop(0)

  for num in nums:
    t = (t + num) / 2

  print(t)

  return None


def B():
  return None


def C():
  return None


MAIN()
