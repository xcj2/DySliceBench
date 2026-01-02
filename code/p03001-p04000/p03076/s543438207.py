def ii2ss(n):
    ss = []
    for i in range(n):
        ss.append(input())
    return ss

def sp2nn(sp, sep=' '):
    return [int(s) for s in sp.split(sep)]

def ss2nn(ss):
    return [int(s) for s in list(ss)]

import math
def main(ss):
    nn = ss2nn(ss)
    total = 0
    mod = 0
    for n in nn:
        n2 = math.ceil(n/10)*10
        total += n2
        m = n % 10
        if m != 0:
            if mod == 0:
                mod = m
            elif m < mod:
                mod = m
    if mod != 0:
        total -= 10 - mod
    return total
ss = ii2ss(5)
print(main(ss))