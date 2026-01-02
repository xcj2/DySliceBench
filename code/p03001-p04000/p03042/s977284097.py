from io import StringIO
from collections import *
from functools import *
import sys


def main(inputs):
    n = int(next(inputs))
    # xs = list(map(int, next(inputs).split()))
    n0 = n // 100
    n1 = (n % 100)

    if ismonth(n0) and ismonth(n1):
        return "AMBIGUOUS"

    if ismonth(n0):
        return "MMYY"

    if ismonth(n1):
        return "YYMM"
    
    return "NA"

def ismonth(m):
    return 0 < m and m <= 12


def gen_inputs(str_=None):
    inputs = StringIO(str_) if str_ else sys.stdin
    while True:
        a = inputs.readline().rstrip()
        yield a
        pass
    pass


if __name__ == "__main__":
    print(main(gen_inputs()))
    pass
