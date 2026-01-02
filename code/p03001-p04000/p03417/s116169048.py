# ABC090C 3/18
import numpy as np
#import math
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0]*n
def zeros2(n, m): return [zeros(m)]*n # obsoleted zeros((n, m))で代替
def getIntLines(n): return [int(input()) for i in range(n)]
def getIntMat(n, m):  # n行に渡って、1行にm個の整数
    mat = zeros2(n, m)
    for i in range(n):
        mat[i] = getIntList()
    return mat
class Debug():
    def __init__(self):
        self.debug = True

    def off(self):
        self.debug = False

    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                print(cmt, ':  ', end='')
            print(x)
        return x


def prob():
    d = Debug()
    d.off()
    N, M = getIntList()
    d.dmp((N, M))
    n = abs(N-2)
    m = abs(M-2)
    d.dmp((n,m),'n,m')
    return n*m


ans = prob()
if ans is None:
    pass
elif type(ans) == list and ans[0] == 'col':
    for elm in ans[1]:
        print(elm)
else:
    print(ans)
