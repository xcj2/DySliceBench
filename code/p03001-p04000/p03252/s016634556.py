import sys
import socket

hostname = socket.gethostname()

if hostname == 'F551C':
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
    S = read_str()
    T = read_str()
    n = len(S)
    res = 'Yes'
    A = [0] * n
    B = [0] * n
    vu = {}
    for i in range(n):
        if S[i] in vu:
            A[i] = vu[S[i]]
        else:
            vu[S[i]] = i
            A[i] = vu[S[i]]

    vu = {}
    for i in range(n):
        if T[i] in vu:
            B[i] = vu[T[i]]
        else:
            vu[T[i]] = i
            B[i] = vu[T[i]]

    if A != B:
        res = 'No'

    # for i in range(n):
    #     for j in range(n):
    #         if S[i] != S[j] and T[i] == T[j]:
    #             res = 'No'
    #         if S[i] == S[j] and T[i] != T[j]:
    #             res = 'No'
    print(res)


main()
