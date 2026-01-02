import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    K=I()
    L=[]
    import queue
    
    
    q=queue.Queue()
    for i in range(1,10):
        q.put(i)
        
    dx=[-1,0,1]
        
        
    while len(L)!=K:
        a=q.get()
        L.append(a)
        res=a%10
        for i in range(3):
            c=dx[i]
            res2=res+c
            if res2!=-1 and res2!=10:
                new=a*10+res2
                q.put(new)
                
    print(L[-1])
                

main()
