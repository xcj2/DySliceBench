fact = [1]
for i in range(20):
    fact.append(fact[-1] * (i+1))

def calc(L):
    NN = 17
    BIT=[0]*(2**NN+1)
    def addbit(i):
        while i <= 2**NN:
            BIT[i] += 1
            i += i & (-i)
    def getsum(i):
        ret = 0
        while i != 0:
            ret += BIT[i]
            i -= i&(-i)
        return ret
    re = 0
    for i, a in enumerate(L[::-1]):
        re += getsum(a) * fact[i]
        addbit(a)
    return re

N = int(input())
P = [int(a) for a in input().split()]
Q = [int(a) for a in input().split()]
 
print(abs(calc(P) - calc(Q)))