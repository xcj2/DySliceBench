def main():
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    f=sorted(list(map(int,input().split())),reverse=True)
    def b_search(a,b,value,lim):
        med=(a+b)//2
        if a==b:return a
        elif lim=="upper":
            if a+1==b:
                if value(b):return b
                else:return a
            elif value(med):return b_search(med,b,value,lim)
            else:return b_search(a,med-1,value,lim)
        else:
            if a+1==b:
                if value(a):return a
                else:return b
            elif value(med):return b_search(a,med,value,lim)
            else:return b_search(med+1,b,value,lim)

    def count(val):
        cnt=0
        for i in range(n):
            cnt+=max(a[i]-val//f[i],0)
        if cnt>k:
            return False
        else:
            return True
    
    print(b_search(0,10**12+10,count,"lower"))
    
main()