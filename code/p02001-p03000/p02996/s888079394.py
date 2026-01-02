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
30
384 8895
1725 9791
170 1024
4 11105
2 6
578 1815
702 3352
143 5141
1420 6980
24 1602
849 999
76 7586
85 5570
444 4991
719 11090
470 10708
1137 4547
455 9003
110 9901
15 8578
368 3692
104 1286
3 4
366 12143
7 6649
610 2374
152 7324
4 7042
292 11386
334 5720
'''


def MAIN():
  # T_IN()
  if A():
    print("Yes")
  else:
    print("No")


def A():
  n = IN_I()
  # [[a, b]]
  md = list([IN_L_I() for i in range(0, n)])
  md.sort(key=lambda x: (x[1]))
  total = 0
  for item in md:
    total += item[0]
    if total > item[1]:
      return False


  return True


def B():
  return None


def C():
  return None


MAIN()
