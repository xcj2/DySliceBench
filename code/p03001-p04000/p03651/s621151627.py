from math import gcd
from functools import reduce


def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K > max(A):
        print('IMPOSSIBLE')
        exit()
    if N == 1:
        if A[0] == K:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')
        exit()
    
    A.sort()
    B = A[0]
    for i in range(N):
        B = gcd(B, A[i])

    if B == 1:
        print('POSSIBLE')
        exit()
    
    if K % B == 0:
        print('POSSIBLE')
        exit()

    print('IMPOSSIBLE')

    



if __name__ == "__main__":
    main()