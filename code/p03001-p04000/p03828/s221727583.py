import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    
    #nの素因数分解，[[a1,b1],[a2,b2]...]   aがb個,
    def factorization(n):
        if n==1:
            return [0,1]
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])

        if temp!=1:
            arr.append([temp, 1])

        if arr==[]:
            arr.append([n, 1])

        return arr
    
    N=I()
    ans=1
    L=[0]*(N+1)
    for i in range(2,N+1):
        arr=factorization(i)
        for j in range(len(arr)):
            L[arr[j][0]]+=arr[j][1]
    
    for i in range(len(L)):
        ans*=(L[i]+1)
        ans%=mod
    print(ans)
    

main()
