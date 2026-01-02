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
5
1 3 5 4 2
'''


def MAIN():
  # T_IN()
  A()


def A():
  s = IN_I()
  l = IN_L_I()

  r = [0] * s

  p = l[0]
  pc = 0
  m = l[0]
  mc = 0

  for num in l[1:]:
    if num < p:
      pc += 1
    else:
      r[pc] += 1
      pc = 0

    if num > m:
      mc += 1
    else:
      r[mc] += 1
      mc = 0

    p = num
    m = num

  r[pc] += 1
  r[mc] += 1

  ret = 0
  for i, count in enumerate(r[2:]):
    ret += (i + 1) * count

  print(ret)

def B():
  return None


def C():
  return None


MAIN()
