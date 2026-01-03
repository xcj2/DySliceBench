def examC():
    St = S()
    N = len(St)
    cur = int(0)
    ansC = [0]*(2**(N-1))
    for i in range(2**(N-1)):
        k = int(0)
        cur = int(0)
        for j in range(N-1):
            if (i>>j)%2==1:
#                print(St[k:j+1],i,j)
                cur += int(St[k:j+1])
                k = j+1
        cur += int(St[k:])
        ansC[i] = cur

    print(sum(ansC))

import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
