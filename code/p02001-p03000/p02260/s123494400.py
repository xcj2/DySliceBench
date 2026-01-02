import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    N = sc.intarr()[0]
    A = sc.intarr()

    count = 0

    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            count += 1
    display(A)
    print(count)


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

