
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    R,S,P=MI()
    T=input()
    L=[]
    
    ans=0
    for i in range(N):
        pre="z"
        if i-K>=0:
            pre=L[i-K]
            
        if T[i]=="r":
            if pre!="p":
                ans+=P
                L.append("p")
            else:
                L.append("z")
                
        if T[i]=="s":
            if pre!="r":
                ans+=R
                L.append("r")
            else:
                L.append("z")

        if T[i]=="p":
            if pre!="s":
                ans+=S
                L.append("s")
            else:
                L.append("z")
                
    print(ans)
                
    

main()
