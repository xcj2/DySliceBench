import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n, k, q = sc.intarr()
    member = [k-q] * n
    for i in range(q):
        member[sc.intarr()[0]-1] += 1

    for i in member:
        if i > 0:
            print('Yes')
        else:
            print('No')


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
