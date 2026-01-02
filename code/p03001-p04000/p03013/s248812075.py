import sys
import math
input = sys.stdin.readline


def main():
    MOD = 10 ** 9 + 7
    sc = Scan()
    n, m = sc.intarr()
    w = sc.intarr_ver(m)
    is_safe = [True] * (n+2)
    for a in w:
        is_safe[a + 1] = False
    dp = [0] * (n+2)
    dp[1] = 1
    for i in range(2, n+2):
        if is_safe[i]:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD
        else:
            dp[i] = 0

    print(dp[n+1])


class Scan():

    def intarr(self):
        line = input()
        array = line.split(' ')
        num_array = [int(n) for n in array]
        return num_array

    def intarr_ver(self, n):
        return [int(input()) for _ in range(n)]

    def strarr(self):
        line = input()
        array = line.split(' ')
        array[-1] = array[-1].strip('\n')
        return array


main()
