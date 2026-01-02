import sys
sys.stdin.readline
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

def main():
    c=[[]for _ in range(3)]
    for i in range(3):
        c[i]=LI()
    a=[0,0,0]
    b=[0,0,0]
    for i in range(3):
        b[i]=c[0][i]
        
    for i in range(1,3):
        a[i]=c[i][0]-b[0]
        
    flag=1
    
    for i in range(3):
        for j in range(3):
            if c[i][j]!=a[i]+b[j]:
                flag=0
                
    if flag==1:
        print("Yes")
    else:
        print("No")
        
    
            
    


main()