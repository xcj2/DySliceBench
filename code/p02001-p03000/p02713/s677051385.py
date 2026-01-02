#MLE注意！

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    k = int(input())
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    def gcd_group(arr):
        g = gcd(arr[0], arr[1])
        for i in range(2, len(arr)):
            g = gcd(g, arr[i])
        return g
    
    def lcm(a, b):
        g = gcd(a, b)
        return (a*b)//g
    
    def lcm_group(arr):
        l = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            l = lcm(l, arr[i])
        return l
    
    res = 0
    for a in range(1, k+1):
        for b in range(a, k+1):
            for c in range(b, k+1):
                if a==b==c:
                    res += gcd_group([a,b,c]) 
                elif a==b or b==c or a==c:
                    res += gcd_group([a,b,c]) * 3
                else:
                    res += gcd_group([a,b,c]) * 6
    print(res)

if __name__ == '__main__':
    main()