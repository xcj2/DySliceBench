#!python3

import sys

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, Q = iim()
    A = [0] * (N+1)
    la = N + 1

    def add(i, x):
        while i < la:
            A[i] += x
            i += i & -i

    def getSum(i):
        ans = 0

        while i:
            ans += A[i]
            i -= i & -i

        return ans

    ans = []
    for com, *arg in (map(int, line.split()) for line in sys.stdin):
        if com == 0:
            add(*arg)
        else:
            #print("+", *arg)
            ans.append(getSum(arg[1]) - getSum(arg[0]-1))
        #print(A)
    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()

