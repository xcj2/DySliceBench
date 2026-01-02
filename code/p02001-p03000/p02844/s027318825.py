import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    _ = sc.intarr()[0]
    S = sc.strarr()[0]

    count = 0

    for i in range(1000):
        # print("--------")
        lucky = format_str(i)
        first = S.find(lucky[0])
        third = S.rfind(lucky[2])

        if first == -1 or third == -1:
            continue
        elif first < third:
            if lucky[1] in S[first + 1:third]:
                count += 1
    print(count)


def format_str(num):
    if num < 10:
        return "00" + str(num)
    elif num < 100:
        return "0" + str(num)
    else:
        return str(num)


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
