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
5 2
'''


def MAIN():
  # T_IN()
  A()


def A():
  n, l = IN_L_I()
  li = list([ i + l for i in range(0,  n)])
  if li.count(0) == 0:
    j = li.pop(0)
    k = li.pop(-1)
    if abs(j) < abs(k):
      li.append(k)
    else:
      li.append(j)

  print(sum(li))

  return None
 

def B():
  return None


def C():
  return None


MAIN()
