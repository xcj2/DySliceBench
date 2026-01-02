import sys
input = sys.stdin.readline

# from collections import deque

def linput(_t=int): return list(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    # N = int(input())
    # A = int(input())
    A,B,C = linput(str)
    # B,C = linput()
    # S = input()

    # vA = linput()
    # S = input()
    # mX = [linput() for _ in [0,]*N]

    # res = 0
    # res = sum(int(a) for a in (A,B,C))
    # print(res)
    print(C,A,B)
    # print(("No","Yes")[res%2])


main()
