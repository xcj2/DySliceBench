import numpy as np

DEBUG = False

def dprint(*args):
    if DEBUG:
        print(*args)

digit = 6

def to_str(x):
    if x[0] == 0:
        return str(x[1])
    else:
        return "{:d}{:06d}".format(x[0], x[1])


def add(x, y):
    carry = 0
    new1 = x[1] + y[1]
    if new1 >= 1000000:
        carry = 1
        new1 -= 1000000
    new0 = x[0] + y[0] + carry
    return [new0, new1]

def sub(x, y):
    carry = 0
    new1 = x[1] - y[1]
    if new1 < 0:
        carry = 1
        new1 += 1000000
    new0 = x[0] - y[0] - carry
    return [new0, new1]

def gt(x, y):
    if x[0] > y[0]:
        return True
    elif x[0] < y[0]:
        return False
    else:
        if x[1] > y[1]:
            return True
        else:
            return False

abk = input().split(' ')
a_s, b_s, k_s = abk

nums = []
for t_str in abk:
    if len(t_str) > 6:
        upper, lower = int(t_str[0:-6]), int(t_str[-6:])
    else:
        upper, lower = 0, int(t_str)
    nums.append([upper, lower])

a, b, k = nums
dprint(a_s, b_s, k_s)
dprint(a, b, k)
dprint(gt(a, b))
dprint(gt(b, a))
dprint(gt(a, k))
dprint(gt(k, a))

if(gt(a, k)):
    result = sub(a, k)
    print(to_str(result), b_s)
else:
    mod = sub(k, a)
    if(gt(b, mod)):
        mod2 = sub(b, mod)
        print(0, to_str(mod2))
    else:
        print(0, 0)
