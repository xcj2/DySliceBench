def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys,heapq,math
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    out = sys.stdout.write
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9)+7

    n=int(data())
    A=list(mdata())
    d1=dd(int)
    d2=dd(int)
    for i in range(n):
        if i+1+A[i]<n:
            d1[i+1+A[i]]+=1
        if i+1-A[i]>1:
            d2[i+1-A[i]]+=1
    ans=0
    for i in d1:
        ans+=d1[i]*d2[i]
    print(ans)

if __name__ == '__main__':
    main()
