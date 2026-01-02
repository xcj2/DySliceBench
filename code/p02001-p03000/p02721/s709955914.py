
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    #前から見ると最短でできる
    # + 後ろから見ると最遅でできる　→最短でも最遅でも変わらぬ日数で扱うべきなら必須
    N,K,C=MI()
    S=input()
    
    fast=[0]*N
    slow=[0]*N
    inf=10**10
    day=1#何日目にやるか
    i=0
    while i<N:
        if S[i]=="x":
            i+=1
        else:
            fast[i]=day
            day+=1
            i+=C+1
    
    #最遅の場合，後ろから見ているのでdayの順番も逆にしている
    i=N-1
    day=1
    while i>=0:
        if S[i]=="x":
            i-=1
        else:
            slow[i]=day
            day+=1
            i-=C+1
            
            
    ans=[]
    for i in range(N):
        if fast[i]*slow[i]!=0:
            if fast[i]+slow[i]==K+1:
                ans.append(i)
                
                
    for i in range(len(ans)):
        print(ans[i]+1)
            
        
            
            
    
        
    

main()
