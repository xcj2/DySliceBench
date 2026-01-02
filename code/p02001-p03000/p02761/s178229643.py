#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N,M=MI()
    st=pow(10,N-1)
    en=pow(10,N)
    
    if N==1:
        st=0
   
    s=[0]*M
    c=[0]*M
    for i in range(M):
        s[i],c[i]=MI()
        s[i]-=1
   
    ans=-1

   
    for i in range(st,en):
        flag=1
        i2=str(i)
        
        for j in range(M):
            aaa=int(i2[s[j]])
            if aaa!=c[j]:
                flag=0
                break
               
        if flag:
            ans=i
            break
        
    print(ans)
       
   
main()
