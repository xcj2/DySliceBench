# coding: utf-8
import sys

stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces


def BinarySearch(num, nums):
    if len(nums) == 0:
        print("Erorr : list has no element")
        return
    left,right = 0,len(nums)
    while left < right:
        mid  = (left+right)//2
        if num < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return right


def BitSearch(a):
    n = len(a)
    rets = []
    for i in range(pow(2,n)):
        ret = 0
        for j in range(n):
            if ((i>>j) & 1):
                ret += a[j]
        rets += [ret]
    return rets


def main():
    n = ni()
    a = na()
    aBitSum = sorted(BitSearch(a))
    qn = ni()
    qs = na()
    for q in qs:
        mid = BinarySearch(q,aBitSum)
        if aBitSum[mid-1] == q:
            print('yes')
        else:
            print('no')
    return


if __name__ == '__main__':
    main()
