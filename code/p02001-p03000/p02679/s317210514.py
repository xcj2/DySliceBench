

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    from math import gcd
    from collections import defaultdict
    dd = defaultdict(int)
    temp0=0

    for i in range(N):
        a,b=MI()
        if (a,b)==(0,0):
            temp0+=1
            continue
        
        if a<0:
            a*=-1
            b*=-1
        
        #(+,+)と(+,-)だけにする
        if a*b!=0:
            g=gcd(a,b)
            a=a//g
            b=b//g
            if a*b>0:#(+,+)
                dd[(a,b)]+=1
                dd[b,-a]+=0
                
            else:#(+,-)
                dd[(a,b)]+=1
                dd[(-b,a)]+=0
            
        elif (a,b)!=(0,0):
            #assert 0
            if a==0:
                b=1
            else:
                a=1
                
            dd[(a,b)]+=1
            dd[(b,a)]+=0
        

    ans=1
    
    for k,v in dd.items():
        a,b=k
        if b<=0:
            continue
        #( +,+)と(0,1)だけ見る
        
        if a*b!=0:
            v=dd[k]
            v2=dd[(b,-a)]
        else:
            v=dd[k]
            v2=dd[(b,a)]
        temp=pow(2,v,mod)+pow(2,v2,mod)-1
        
        ans=(ans*temp)%mod

    ans=(ans-1+temp0)%mod
    print(ans)
        
        
            
            
    #せんぶ０の組みをひく
        
    

main()
