def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return map(int, data().split())
    out = sys.stdout.write
    # sys.setrecursionlimit(100000)

    a,b,c,d=mdata()
    k1=a//d
    if a%d!=0:
        k1+=1
    k2=c//b
    if c%b!=0:
        k2+=1
    if k1>=k2:
        print("Yes")
    else:
        print("No")




if __name__ == '__main__':
    main()