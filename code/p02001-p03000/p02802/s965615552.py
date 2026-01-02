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


def main0():
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

    correct = len(r)
    penalties = 0
    f = set()  
    for i in range(M):
      if S[i] == 'AC':
        if p[i] not in f:
          f.add(p[i])
      
      if S[i] == 'WA':
        if p[i] not in f and p[i] in r:
          penalties += 1

    print(correct, penalties)


def main1():
    N, M = read_int_list()
    correct = 0
    penalties = 0
    WA = [0] * (N + 1)
    AC = [0] * (N + 1)
    for i in range(M):
      l = read_str_list()
      p = int(l[0])
      S = l[1]

      if S == 'AC':
        AC[p] += 1
      if S == 'WA':
        WA[p] += 1

      if S == 'AC' and AC[p] == 1:
        correct += 1
        penalties += WA[p]
      
      # print(AC[1:], WA[1:])

    print(correct, penalties)

main1()
