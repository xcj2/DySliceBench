import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    s, t = sc.strarr()
    text = ''

    for ss, tt in zip(s, t):

        text = text + ss
        text = text + tt

    print(text)


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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def natural_num(n):
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            return 0
    return 1


main()
