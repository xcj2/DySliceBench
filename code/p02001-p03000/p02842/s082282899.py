import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N = sc.intarr()[0]
    for i in range(50000):
        inTax = int(i * 1.08)
        if inTax < N:
            continue
        elif inTax == N:
            print(i)
            return
        elif inTax > N:
            print(":(")
            return


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


main()
