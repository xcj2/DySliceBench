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

    n=int(data())
    l1=[]
    l2=[]
    cnt1=0
    cnt2=0
    for i in range(n):
        s=data()
        o=c=0
        for j in s:
            if j=='(':
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    c+=1
        if o==0:
            if c!=0:
                cnt2+=c
        elif c==0:
            cnt1+=o
        else:
            if c>o:
                l2.append([c,o])
            else:
                l1.append([c,o])
    l1.sort(key=lambda x:x[0])
    flag=True
    for i in l1:
        if cnt1>=i[0]:
            cnt1=cnt1-i[0]+i[1]
        else:
            flag=False
            break
    l2.sort(key=lambda x: x[1],reverse=True)
    l2.sort(key=lambda x: x[0],reverse=True)
    for i in l2:
        if cnt1>=i[0]:
            cnt1=cnt1-i[0]+i[1]
        else:
            flag=False
            break
    if flag==True:
        if cnt1-cnt2==0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()
