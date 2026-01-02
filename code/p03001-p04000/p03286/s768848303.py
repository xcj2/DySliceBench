#import sys
#input = sys.stdin.readline
#template input
import bisect

def IT():
    return int(input())
def IL():
    return [int(_) for _ in input().split()]
def SL():
    return [int(_) for _ in input().split()]
def ILS(n):
    return [int(input()) for _ in range(n)]
def SLS(n):
    return [input() for _ in range(n)]
def ILSS(n):
    return [[int(_) for _ in input().split()] for j in range(n)]


"""ここからメインコード"""
def main():
    n = IT()
    ans = ""
    for i in range(32):
      if n % (2 ** (i+1)) != 0:
        n -= n % (2 ** (i+1)) * (-1) ** (i % 2)
        ans += "1"
      else:
        ans += "0"
    print(int(ans[::-1]))
main()

