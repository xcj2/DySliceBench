import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    s = sc.strarr()[0]
    if s == 'MON':
        print('6')
    elif s == 'TUE':
        print('5')
    elif s == 'WED':
        print('4')
    elif s == 'THU':
        print('3')
    elif s == 'FRI':
        print('2')
    elif s == 'SAT':
        print('1')
    elif s == 'SUN':
        print('7')


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
