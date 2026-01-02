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


def solve(A, N, b):
    l = [[(0, 0), (0, 1), (0, 2)], 
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]]

    for k in l:
        if all(A[i][j] in b for i, j in k):
          return 'Yes'
    return 'No'


def main():
    A = [read_int_list() for i in range(3)]
    N = read_int()
    b = [read_int() for k in range(N)]
    
    res = solve(A, N, b)
    print(res)


main()
