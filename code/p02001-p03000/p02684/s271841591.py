def main():

    import sys, math
    #from bisect import bisect_left as bl, bisect_right as br, insort
    #from heapq import heapify, heappush, heappop
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9)+7

    n,k=mdata()
    A=mdata()
    cnt=1
    d=dd(int)
    d1=dd(int)
    d[0]=1
    d1[1]=0
    t=0
    while True:
        if d[A[t]-1]==0:
            cnt+=1
            d[A[t]-1]=cnt
            d1[cnt]=A[t]-1
        else:
            ind1=d[A[t]-1]
            ind2=d[t]
            break
        t=A[t]-1
    if k+1<=ind1:
        print(d1[k+1]+1)
    else:
        k+=1
        k-=ind1
        k=k%(ind2-ind1+1)
        print(d1[(ind1+k)]+1)

if __name__ == '__main__':
    main()
