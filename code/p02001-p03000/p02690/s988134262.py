import sys
input = sys.stdin.readline

# from collections import deque

def linput(_t=int):
    return list(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    X = int(input())
    # res = 0
    # for s in S.split("-"):
    #     res = max(res, len(s))

    # print(301**5 - 300**5)

    for A in reversed(range(-310,310)):
        for B in reversed(range(-310,310)):
            if A**5 - B**5 == X:
                print(A, B)
                return
    


    # print(res)

    # print(("No","Yes")[res%2])


main()
