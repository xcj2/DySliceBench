def main():
    n=int(input())
    a=list(map(int,input().split()))
    
    def judge(k):
        cnt=0
        for i in a:
            cnt+=max((i-n+k)//(n+1)+1,0)
        if cnt>k:
            return False
        else:
            return True

    #a,bには下限と上限、valueにはOKな範囲のときはTrue、そうでないときにFalseを返す関数を入れる
    #limは下限を知りたいときはlower、上限を知りたいときはupperを入れる
    def b_search(a,b,value,lim):
        med=(a+b)//2
        if a==b:return a
        elif lim=='upper':
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

    j=b_search(0,10**18,judge,'lower')
    ans=j
    for i in range(j-1,max(j-3000,-1),-1):
        if judge(i):
            ans=i
    print(ans)
main()