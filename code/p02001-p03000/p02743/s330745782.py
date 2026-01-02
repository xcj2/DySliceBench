import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from decimal import *
INF = 10 ** 20

def main():
    a,b,c = getList()
    k = max([a,b,c])
    getcontext().prec = 20  # デフォルト28桁のところを20桁にする
    a = Decimal(a).sqrt()
    b = Decimal(b).sqrt()
    c = Decimal(c).sqrt()
    # if math.sqrt(a/k) + math.sqrt(b/k)  < math.sqrt(c/k):
    if a + b < c:
        print("Yes")
    else:
        print("No")

    # print(math.sqrt(2000000000))
if __name__ == "__main__":
    main()