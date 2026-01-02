import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N, M = sc.intarr()
    array = []
    for i in range(M):
        p, s = sc.strarr()
        array.append([p, s])

    data = {}
    AC_cnt = 0
    WA_cnt = 0
    for ss in array:
        if ss[0] not in data:
            if ss[1] == 'WA':
                data[ss[0]] = [0, 1]
            elif ss[1] == 'AC':
                data[ss[0]] = [1, 0]
        elif data[ss[0]][0] == 0:
            if ss[1] == 'WA':
                data[ss[0]][1] += 1
            elif ss[1] == 'AC':
                data[ss[0]][0] += 1

    for key in data:
        if data[key][0] != 0:
            AC_cnt += 1
            WA_cnt += data[key][1]

    print(AC_cnt, WA_cnt)


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
