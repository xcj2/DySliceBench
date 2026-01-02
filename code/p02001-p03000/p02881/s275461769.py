import math
import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    ns = int(math.sqrt(n)) + 1
    minimum = n
    for i in range(1, ns):
        if n % i == 0:
            cost = (n//i) + i - 2
            if cost < minimum:
                minimum = cost
    print(minimum)


class Scan():

    def intarr(self):
        self.line = input()
        array = self.line.split(' ')
        num_array = [int(n) for n in array]
        return num_array

    def strarr(self):
        self.line = input()
        array = self.line.split(' ')
        array[-1] = array[-1].strip('\n')
        return array


main()
