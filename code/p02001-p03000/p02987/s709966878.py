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
ABBA
'''

def MAIN():
  # T_IN()
  if A():
    print("Yes")
  else:
    print("No")
  quit()

def A():
  s = IN_S()
  l = list(STR_SPLIT(s, 1))
  l.sort()
  if len(l) == 4 and l[0] == l[1] and l[2] == l[3] and l[1] != l[2]:
    return True
  return False


MAIN()
