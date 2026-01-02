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
    A = read_int_list()
    A.sort()
    s = []
    for i in range(N-1):
      if A[i+1] != A[i]:
        s.append(A[i])
    l = len(s)
    if l == N - 1:
      res = 'YES'
    else:
      res = 'NO'
    print(res)


main()
