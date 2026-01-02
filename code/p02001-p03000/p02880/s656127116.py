import sys
input = sys.stdin.readline


def main():
    sc = Scan()
    n = sc.intarr()[0]
    for i in range(1, 10):
        if n % i == 0:
            for j in range(1, 10):
                if i*j == n:
                    print('Yes')
                    quit()
    print('No')


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
