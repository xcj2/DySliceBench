import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N=I()
    L=[]
    R=[]

    
    for i in range(N):
        a,b=MI()
        L.append(a)
        R.append(b)
    L.sort()
    R.sort()
        
    #中央値の最小値は，Lの中央値．中央値の最大値はRの中央値
    #間は全部埋められそう?
        
    if N%2==0:
        Lm=(L[N//2]+L[N//2-1])
        Rm=(R[N//2]+R[N//2-1])
    else:
        Lm=L[N//2]
        Rm=R[N//2]
    ans=Rm-Lm+1
    print(ans)
        
        
        
        
        
    
            

main()
