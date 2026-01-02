import math
import sys
def input():
    return sys.stdin.readline().rstrip('\n')

def get_e(x):
    l = []
    i = 2
    m = math.floor(math.sqrt(x))
    while i <= m and i <= x:
        if x % i == 0:
            x = x // i
            l += [i]
        else:
            i += 1
    if x != 1:
        l += [x]
    return l

def calc(N):
    d = {}
    for i in get_e(N):
        d[i] = 1 + (d[i] if i in d else 0)
    result = 0
    for i in d:
        result += math.floor((math.sqrt(1 + 8 * d[i]) - 1) / 2)
    return result
    

N = int(input())
print(calc(N))