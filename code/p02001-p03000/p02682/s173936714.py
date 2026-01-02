def main():

    import sys, math
    #from bisect import bisect_left as bl, bisect_right as br, insort
    #from heapq import heapify, heappush, heappop
    #from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9)+7

    a,b,c,k=mdata()
    if k>a:
        if k>b:
            print(a-(k-a-b))
        else:
            print(a)
    else:
        print(k)

if __name__ == '__main__':
    main()
