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
    N, M = read_int_list()
    p = [0] * M
    S = [''] * M
    for i in range(M):
      l = read_str_list()
      p[i] = int(l[0])
      S[i] = l[1]
      
    r = set()
    for i in range(M):
      if S[i] == 'AC':
        if p[i] not in r:
          r.add(p[i])

    correct, penalties = 0, 0
    f = set()  
    for i in range(M):
      if S[i] == 'AC':
        if p[i] not in f:
          f.add(p[i])
          correct += 1
      # print(p[i], S[i], f, r)
      
      if S[i] == 'WA':
        if p[i] not in f and p[i] in r:
          penalties += 1

    print(correct, penalties)

main()
