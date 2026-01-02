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
5 2 3 4 1
'''


def MAIN():
  # T_IN()
  if A():
    print("YES")
  else:
    print("NO")


def A():
  n = IN_I()
  l = IN_L_I()
  cnt = 0
  for i, item in enumerate(l):
    if i + 1 != item:
      cnt += 1

  if cnt == 0 or cnt == 2:
    return True
  
  return False


def B():
  return None


def C():
  return None


MAIN()
