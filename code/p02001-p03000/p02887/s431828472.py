import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    s = sc.strarr()[0]
    ans = ''
    before = s[0]
    for i in range(1, n):
        c = s[i]
        if before != c:
            ans += before
            before = c

    ans += before
    print(len(ans))


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
