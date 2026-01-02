import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    D=LI()
    #同じ時差の都市に対して3人以上いる場合は0
    if 0 in D:
        print(0)
        exit()
    if D.count(12)>=2:
        print(0)
        exit()
    
    temp=[0]*24
    temp[0]=1
    if 12 in D:
        temp[12]=1
    
    d=[]
    cnt=0
    for i in range(1,12):
        if D.count(i)==1:
            d.append(i)
            cnt+=1
        elif D.count(i)==2:
            temp[i]=1
            temp[24-i]=1
        elif D.count(i)>=3:
            print(0)
            exit()
            
            
    ans=[]
    
    for i in range(1<<cnt):
        temp2=[0]*24
        
        #コピー
        for k in range(24):
            temp2[k]=temp[k]
        
        for j in range(cnt):
            if i>>j & 1:
                temp2[d[j]]=1
            else:
                temp2[24-d[j]]=1
                
        aaa=24
        for ii in range(24):
            for jj in range(ii+1,24):
                if temp2[ii]==1 and temp2[jj]==1:
                    diff=min(jj-ii,24-(jj-ii))
                    if diff<aaa:
                        aaa=diff
        ans.append(aaa)
    print(max(ans))
            
    
        

main()
