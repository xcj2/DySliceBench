

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    from collections import defaultdict
    dd = defaultdict(int)
    M=10**10

    
    for _ in range(N):
        c=input()
        if "." in c:
            d=c.index(".")
            a=c[:d]
            b=c[d+1:]
            lb=len(b)
            b+="0"*(10-lb)
        else:
            a=c
            b=0
        c=int(a)*M +int(b)
        
        
        if int(a)==0 and int(b)==0:
            dd[10,10]+=1
        else:
            i=0
            j=0
            while c%2==0:
                c=c//2
                i+=1
            while c%5==0:
                c=c//5
                j+=1
            i-=10
            j-=10
            i=min(i,10)
            j=min(j,10)
            dd[(i,j)]+=1

    ans=0
    
    #dd同士の重複に注意
    
    K=[]
    V=[]
    for k,v in dd.items():
        K.append(k)
        V.append(v)
        
    
    for iiii in range(len(K)):
        k=K[iiii]
        v=V[iiii]
    
        ii,jj=k
        for i in range(-10,11):
            for j in range(-10,11):
                if ii+i>=0 and jj+j>=0:
                    if ii==i and jj==j:
                        temp=dd[(i,j)]
                        ans+=temp*(temp-1)
                    else:
                        ans+=dd[(i,j)]*v
        # print(k,v,ans)
                    
                    
                    
    print(ans//2)
            
    

            
                    
                       

 
               

main()
