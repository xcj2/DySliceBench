import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    N = read_int()
    A = read_int_list()
    for i in range(N):
      if A[i] % 2 == 0:
        if not (A[i] % 3 == 0 or A[i] % 5 == 0):
          return 'DENIED'
    return 'APPROVED'


def main():
    res = solve()  
    print(res)


main()
