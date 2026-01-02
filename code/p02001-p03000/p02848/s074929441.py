import sys
import math
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    s = sc.strarr()[0]

    new_str = ''
    for i in s:
        i = ord(i)
        i = i + n
        if i > 90:
            i -= 26
        i = chr(i)
        new_str += i

    print(new_str)


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
