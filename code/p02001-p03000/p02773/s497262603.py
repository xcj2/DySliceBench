import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    N = read_int()
    s = []
    for i in range(N):
      S = read_str()
      s.append(S)
    s.sort()
    s.append('')

    res = []
    M = -1
    m = 1
    for i in range(1, N+1):
      if s[i-1] == s[i]:
        m += 1
      else:
        if m == M:
          res.append(s[i-1])
        if m > M:
          M = m
          res = [s[i-1]]
        m = 1
    print(*res, sep='\n')


main()
