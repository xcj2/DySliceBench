import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    s = sc.strarr()[0]

    index = 0
    for c in s:
        if index % 2 == 0 and c == 'L':
            print('No')
            exit()
        if index % 2 == 1 and c == 'R':
            print('No')
            exit()
        index += 1
    print('Yes')


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
