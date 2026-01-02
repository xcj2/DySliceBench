import itertools
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def main():
    k = int(input())

    ans = 0
    c = list(itertools.combinations_with_replacement(range(1,k+1), 3))
    for elem in c:
        n_gcd = gcd_list(list(elem))
        length = len(set(elem))
        if length == 1:
            k = 1
        elif length == 2:
            k = 3
        elif length == 3:
            k = 6
        ans += k * n_gcd 
    print(ans)

if __name__ == '__main__':
    main()