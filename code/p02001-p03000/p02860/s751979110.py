import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    s = sc.strarr()[0]
    s1 = s[0:(n//2)]
    s2 = s[(n//2):]
    if s1 == s2:
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
