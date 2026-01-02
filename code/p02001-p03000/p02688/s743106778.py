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

    n,k=mdata()
    l=[0]*n
    for i in range(k):
        d=int(data())
        s=mdata()
        for j in s:
            l[j-1]+=1
    cnt=0
    for i in l:
        if i==0:
            cnt+=1
    print(cnt)


if __name__ == '__main__':
    main()
