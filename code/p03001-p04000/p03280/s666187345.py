import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    a, b = sc.intarr()

    ans = (a-1) * (b-1)

    print(ans)


def format_str(num):
    if num < 10:
        return "00" + str(num)
    elif num < 100:
        return "0" + str(num)
    else:
        return str(num)


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
