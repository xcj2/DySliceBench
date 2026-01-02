import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    inf=10**20
    N=I()
    A=LI()
    """左から見ていく，i個を見たときに，
    i//2 ±1の範囲なので，状態は3N通り
    """
    
    p1=[-inf]*N
    zero=[-inf]*N
    n1=[-inf]*N
    
    p1[0]=A[0]
    zero[0]=0
    zero[1]=max(A[0],A[1])
    n1[1]=0
    
    for i in range(2,N):
        #偶奇で遷移の仕方に変化
        if i%2==0:
            p1[i]=max(p1[i-2]+A[i],p1[i-1])#2つ前の状態から取る or 1つ前の状態から取らない
            zero[i]=max(zero[i-2]+A[i],zero[i-1])
            n1[i]=max(n1[i-2]+A[i],n1[i-1])
        else:
            p1[i]=p1[i-2]+A[i]
            zero[i]=max(zero[i-2]+A[i],p1[i-1])
            n1[i]=max(n1[i-2]+A[i],zero[i-1])
            
    """        
    print(p1)
    print(zero)
    print(n1)"""
    
    print(zero[-1])
    
    
        
        
        

main()
