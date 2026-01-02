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
    X = read_int()
    n = 10 ** 6
    for i in range(X, n):
      is_prime = True     
      for d in range(2, X):
          if i % d == 0:
            is_prime = False
      if is_prime:
        print(i)
        break


main()
