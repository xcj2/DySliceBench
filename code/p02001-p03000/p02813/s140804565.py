import sys
import socket
import itertools

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
    P = read_int_list()
    Q = read_int_list()
    i = 1
    for p in itertools.permutations(range(1, N+1)):
      if P == list(p):
        a = i
      if Q == list(p):
        b = i
      i += 1
    res = abs(a - b)
    print(res)


main()
