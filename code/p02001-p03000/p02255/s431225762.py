import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    array = sc.intarr()

    for i in array:
        if i == array[-1]:
            print(i, end='')
        else:
            print(i, end=' ')
    print("")

    for i in range(1, n):
        v = array[i]
        j = i - 1

        while j >= 0 and array[j] > v:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = v
        for i in array:
            if i == array[-1]:
                print(i, end='')
            else:
                print(i, end=' ')
        print("")


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

