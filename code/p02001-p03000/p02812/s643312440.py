import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N = sc.intarr()[0]
    S = sc.strarr()[0]

    count = 0
    flag = 0
    for i in range(N):
        if S[i] == "A":
            flag = 1
        elif flag == 1 and S[i] == "B":
            flag = 2
        elif flag == 2 and S[i] == "C":
            count = count + 1
            flag = 0
        else:
            flag = 0

    print(count)


def dfs(N):
    global dp
    if N <= 0:
        return 1

    if dp[N] > -1:
        return dp[N]
    ans = 0
    for i in range(1, 7):
        ans += dfs(N-i)
    dp[N] = ans
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
