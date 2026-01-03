import sys
import math
input = sys.stdin.readline

used = []
connect = []
N = 0
M = 0


def main():
    global used
    global connect
    global N
    global M
    sc = Scan()
    N, M = sc.intarr()
    a = [0] * M
    b = [0] * M
    for i in range(M):
        aa, bb = sc.intarr()
        a[i] = aa - 1
        b[i] = bb - 1
    connect = [[0] * N for i in range(N)]
    used = [0] * N
    for i in range(M):
        connect[a[i]][b[i]] = 1
        connect[b[i]][a[i]] = 1

    print(dfs(0, 1))


def dfs(now, depth):
    global used
    global connect
    if used[now] == 1:
        return 0

    if depth == N:
        return 1
    ans = 0
    used[now] = 1
    for i in range(N):
        if connect[now][i] == 1:
            ans += dfs(i, depth+1)
    used[now] = 0
    return ans


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
