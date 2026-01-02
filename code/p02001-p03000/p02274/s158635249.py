import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

def InversionNumber(lst):
    bit=BitSum(max(lst))
    res=0
    for i,a in enumerate(lst):
        res+=i-bit.sum(a)
        bit.update(a,1)
    return res

def main():
    n=int(input())
    aa=list(map(int, input().split()))
    s=set()
    for a in aa:
        s.add(a)
    atob={}
    for i,a in enumerate(sorted(s)):
        atob[a]=i+1
    bb=[]
    for a in aa:
        bb.append(atob[a])
    #print(bb)
    print(InversionNumber(bb))

main()

