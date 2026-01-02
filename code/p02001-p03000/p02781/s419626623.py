import sys
import socket

hostname = socket.gethostname()

if hostname in ['F451C', 'N551J']:
    sys.stdin = open('e1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()

def solve(N, K):
  s = list(reversed(str(N)))
  a = [i for i in range(len(s)) if s[i] != '0']
  c = [int(s[i]) for i in range(len(s)) if s[i] != '0']

  # print(a)
  # print(c)
  res = 0
  if K == 1:
    for p in range(100):
      if p == a[-1]:
        res += c[-1]
      if p < a[-1]:
        res += 9

  if K == 2:
    for p in range(100):
      for q in range(p):
        if p < a[-1]:
          res += 9 * 9
        if p == a[-1]:
          if len(a) >= 2:
            if q < a[-2]:
              res += c[-1] * 9
            if q == a[-2]:
              res += (c[-1] - 1) * 9 + c[-2]
            if q > a[-2]:
              res += (c[-1] - 1) * 9
          if len(a) == 1:
            res += (c[-1] - 1) * 9

  if K == 3:
    for p in range(100):
      for q in range(p):
        for r in range(q):
          if p < a[-1]:
            res += 9 * 9 * 9
          if p == a[-1]:
            if len(a) >= 3:
              if q < a[-2]:
                res += c[-1] * 9 * 9
              if q == a[-2]:
                if r < a[-3]:
                  res += (c[-1] - 1) * 9 * 9
                  res += 1 * (c[-2] - 1) * 9
                  res += 1 * 1 * 9
                if r == a[-3]:
                  res += (c[-1] - 1) * 9 * 9
                  res += 1 * (c[-2] - 1) * 9
                  res += 1* 1 * c[-3]
                if r > a[-3]:
                  res += (c[-1] - 1) * 9 * 9
                  res += 1 * (c[-2] - 1) * 9
                  
              if q > a[-2]:
                res += (c[-1] - 1) * 9 * 9
            if len(a) == 2:
              if q < a[-2]:
                res += c[-1] * 9 * 9
              if q == a[-2]:
                res += (c[-1] - 1) * 9 * 9
                res += 1 * (c[-2] - 1) * 9
              if q > a[-2]:
                res += (c[-1] - 1) * 9 * 9
            if len(a) == 1:
              res += (c[-1] - 1) * 9 * 9


  return res


def solve_correct_but_slow(N, K):
  res = 0
  for i in range(1, N+1):
    s = str(i)
    nonzero = len(s) - s.count('0')
    if nonzero == K:
      res += 1
  return res


def find_mismatch():
  N = 1
  while True:
    for K in range(1, 4):
      expected = solve_correct_but_slow(N, K)
      output = solve(N, K)


      if output == expected:
        # print('   N, K, expected, output:', end=' ')
        # print(N, K, expected, output)
        continue

      print()
      print('N, K, expected, output:', end=' ')
      print(N, K, expected, output)
      return
    N += 1




def main():
    N = read_int()
    K = read_int()
    res = solve(N, K)
    print(res)

# find_mismatch()
main()
