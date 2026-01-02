import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    from math import gcd
    
    # 篩の応用でnまでの数全部を素因数分解する
    
    # nまでの素数を列挙(n loglogn)
    n = 10**6 + 5
    
    D=[1]*(n+1) # 篩をしたときに初めて割った数

    #is_prime[i]にはi+1が素数か否かを示すboolが入る，[0]に1の素数判定がある(1-index)．
    is_prime = [True]*(n+1)
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            D[i-1]=i
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                if D[j-1]==1: # D[j-1]にはその数を初めて割れる数を入れとく
                    D[j-1]=i
                j += i

    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    P=[[]for _ in range(n)]
    
    # print(D)
    for i in range(2,n):
        if is_prime[i-1]:
            P[i-1].append(i)
        else:
            now=i
            while now >= 2:
                # print(i,D[now-1])
                P[i-1].append(D[now-1])
                now=now//D[now-1]

    # for i in range(100):
    #     print(i+1,P[i])
    
    N=I()
    A=LI()
    from collections import defaultdict
    dd = defaultdict(int)
    flag=1
    for i in range(N):
        a=A[i]
        S=set(P[a-1])
        # print(a,S)
        for p in S:
            if dd[p]:
                flag=0
                break
            dd[p]+=1
    

            
    if flag:
        print("pairwise coprime")
    else:
        g=A[0]
        for i in range(1,N):
            g=gcd(g,A[i])
        if g==1:
            print("setwise coprime")
        else:
            print("not coprime")
                
            
    

main()
