import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    a, b = sc.intarr()
    print(gcd(a, b))


def gcd(a, b):
    a, b = b, a % b
    if b == 0:
        return a
    else:
        return gcd(a, b)


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


main()

