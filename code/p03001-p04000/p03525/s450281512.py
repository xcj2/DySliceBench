def main():
    from collections import Counter
    def check(l):
        ll=[]
        for i in range(24):
            if l[i]:
                ll.append(i)
                ll.append(i+24)
        ll.sort()
        return min([ll[i+1]-ll[i] for i in range(len(ll)-1)])

    def dfs(d_dfs,l_dfs):
        if len(d_dfs)==0:
            return check(l_dfs)
        l_dfs1=[i for i in l_dfs]
        l_dfs2=[i for i in l_dfs]
        d_dfs1=[i for i in d_dfs]
        i=d_dfs1.pop()
        l_dfs1[i]=True
        l_dfs2[24-i]=True
        return max(dfs(d_dfs1,l_dfs1),dfs(d_dfs1,l_dfs2))

    n=int(input())
    a=list(map(int,input().split()))
    a=Counter(a)
    d=[]
    now=[False]*24
    now[0]=True
    if a[0]>0 or a[12]>1:
        print(0)
        return 0
    if a[12]==1:
        now[12]=True
    for i in range(1,12):
        if a[i]>2:
            print(0)
            return 0
        elif a[i]==2:
            now[i]=True
            now[24-i]=True
        elif a[i]==1:
            d.append(i)
    print(dfs(d,now))
main()