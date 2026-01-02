import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    array = []
    for i in range(n):
        array.append(sc.intarr()[0])
    sorted_array = sorted(array)
    maximum = sorted_array[-1]

    for i in array:
        if i == maximum:
            print(sorted_array[-2])
        else:
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
