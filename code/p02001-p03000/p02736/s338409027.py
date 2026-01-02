
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N=I()
    a2=input()
    a=[]
    for i in range(len(a2)):
        a.append(int(a2[i]))
    
    def calc(L):
        L1=list(L)
        nL=len(L)
        if nL%2==1 or nL<=5000:
            for i in range(nL-1):
                L1[i]=abs(L[i]-L[i+1])
            L1.pop()
                
            return L1
        else:
            L2=[]
            for i in range(0,nL,2):
                L2.append(abs(L[i]-L[i+1]))
            return L2

    while len(a)!=1:
        a=calc(a)    
    
    print(a[0])
                
        
    
main()
