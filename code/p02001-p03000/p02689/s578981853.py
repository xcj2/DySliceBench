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

    n,m=mdata()
    H=mdata()
    l=[1]*n
    for i in range(m):
        a,b=mdata()
        if H[a-1]<H[b-1]:
            l[a-1]=0
        elif H[a-1]>H[b-1]:
            l[b-1]=0
        else:
            l[a-1]=0
            l[b-1]=0
    cnt=0
    for i in l:
         if i==1:
             cnt+=1
    print(cnt)

if __name__ == '__main__':
    main()
