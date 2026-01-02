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
1234
'''


def MAIN():
  # T_IN()
  A()


def A():
  s = IN_S()

  p = ""
  for i in s:
    if len(p) != 0:
      if p == i:
        print("Bad")
        exit()
    p = i

  print("Good")


  return None
 

def B():
  return None


def C():
  return None


MAIN()
