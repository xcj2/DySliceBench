import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    l, r = sc.intarr()
    if r - l >= 2019:
        print('0')
        exit()
    minimum = 2019
    for i in range(l, r):
        for j in range(i+1, r+1):
            num = (i*j) % 2019
            if num < minimum:
                minimum = num
                if minimum == 0:
                    print('0')
                    exit()
    print(minimum)


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
