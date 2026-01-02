import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    sc.intarr()[0]
    h = sc.intarr()
    before = 0
    flag = False
    for i in h:
        if before - i >= 2:
            print('No')
            exit()
        if before - i >= 1:
            if flag:
                print('No')
                exit()
            flag = True
        if before - i < 0:
            flag = False
        before = i
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
