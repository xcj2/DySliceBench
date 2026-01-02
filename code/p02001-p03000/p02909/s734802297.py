import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    s = sc.strarr()[0]

    if s == 'Sunny':
        print('Cloudy')
    elif s == 'Cloudy':
        print('Rainy')
    elif s == 'Rainy':
        print('Sunny')
    else:
        print('error')


class Scan():

    def intarr(self):
        line = input()
        array = line.split(' ')
        num_array = [int(n) for n in array]
        return num_array

    def strarr(self):
        line = input()
        array = line.split(' ')
        array[-1] = array[-1].strip('\n')
        return array


main()
