import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    sc.intarr()[0]
    h = sc.intarr()
    maximum = 0
    count = 0
    before = 0
    for i in h:
        if before < i:
            if maximum < count:
                maximum = count
            count = 0
        else:
            count += 1
        before = i
    if maximum < count:
        maximum = count
    print(maximum)


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
