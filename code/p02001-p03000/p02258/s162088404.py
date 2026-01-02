import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    array = sc.intarr_ver(n)

    minimum = array[0]
    ans = -1000000001
    for i in range(1, n):
        if array[i] - minimum > ans:
            ans = array[i] - minimum
        if array[i] < minimum:
            minimum = array[i]

    print(ans)


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

