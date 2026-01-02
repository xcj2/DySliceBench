import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N = sc.intarr()[0]
    T = []
    S = []
    for i in range(N):
        title, sec = sc.strarr()
        S.append(int(sec))
        T.append(title)
    X = sc.strarr()[0]
    idx = -1
    ans = 0
    for i in range(N):
        if idx != -1:
            ans += S[i]
        if T[i] == X:
            idx = i

    print(ans)


def perm(p):
    if len(p) == 1:
        return [p]
    else:
        s = []
        for i in range(len(p)):
            q = p[i]
            r = perm(p[:i]+p[i+1:])
            for t in r:
                s.append([q] + t)
        return s


class Scan():

    def intarr(self):
        num_array = list(map(int, input().split()))
        return num_array

    def intarr_ver(self, n):
        return [int(input()) for _ in range(n)]

    def strarr(self):
        line = input()
        array = line.split(' ')
        array[-1] = array[-1].strip('\n')
        return array


def display(array):
    for a in range(len(array)):
        if len(array) - a != 1:
            print(array[a], end=' ')
        else:
            print(array[a])


def gcd(a, b):  # 最大公約数
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):  # 最小公倍数
    return a * b // gcd(a, b)


main()
