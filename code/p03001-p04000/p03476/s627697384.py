def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

Q=I()

#nまでの素数を列挙(n loglogn)
n = 10**5

#is_prime[i]にはi-1が素数か否かを示すboolが入る，[0]に1の素数判定がある．
is_prime = [True]*(n+1)
is_prime[0] = False

for i in range(2, n+1):
    if is_prime[i-1]:
        j = 2 * i
        while j <= n:
            is_prime[j-1] = False
            j += i

table = [ i for i in range(1, n+1) if is_prime[i-1]]

L=[]

for p in table:
    p2=(p+1)//2
    if p2 in table:
        L.append(p)
        
S=[0]*(n+1)

for a in L:
    S[a]+=1
    
for i in range(n):
    S[i+1]+=S[i]
    
    
for i in range(Q):
    l,r=MI()
    print(S[r]-S[l-1])
    



