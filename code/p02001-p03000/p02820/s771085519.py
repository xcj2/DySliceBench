import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve(t, R, S, P):
    n = len(t)
    m = [[0] * 3 for i in range(n)]
    m[0][0] = R if t[0] == 's' else 0
    m[0][1] = S if t[0] == 'p' else 0
    m[0][2] = P if t[0] == 'r' else 0

    for i in range(1, n):
      m[i][0] = max(m[i-1][1], m[i-1][2])
      m[i][0] += R if t[i] == 's' else 0
      m[i][1] = max(m[i-1][0], m[i-1][2])
      m[i][1] += S if t[i] == 'p' else 0
      m[i][2] = max(m[i-1][0], m[i-1][1])
      m[i][2] += P if t[i] == 'r' else 0

    return max([m[n-1][0], m[n-1][1], m[n-1][2]])


def bigger(l):
  if l == 'r':
    return 'p'
  if l == 'p':
    return 's'
  if l == 's':
    return 'r'


def solve_greedy(t, R, S, P):
    n = len(t)
    res = 0
    l = ''
    score = {'r': R, 's': S, 'p': P}
    for i in range(n):
      for k in 'rps':
        if t[i] == k:
          if l != bigger(k):
            l = bigger(k)
            res += score[bigger(k)]
          else:
            for q in 'rps':
              if q != bigger(k):
                if i+1 < n and bigger(t[i+1]) != q:
                  l = q
    return res


def main():
    N, K = read_int_list()
    R, S, P = read_int_list()
    T = read_str()

    res = 0
    for i in range(K):
      # res += solve(T[i::K], R, S, P)
      res += solve_greedy(T[i::K], R, S, P)
    
    print(res)


main()
