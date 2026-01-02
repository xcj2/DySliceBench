import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

class BinaryIndexedTree():

    def __init__(self,init_val):
        self.bit = [0] + init_val
        self.n  = len(init_val)

    def sum(self,i):
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= (i & -i)
        return ret
    
    def add(self,i,x):
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = sorted(A)
    dic = {b:i for i,b in enumerate(B,1)}
    bit = BinaryIndexedTree([0]*N)
    ans = 0
    for i,a in enumerate(A):
        ans += i - bit.sum(dic[a])
        bit.add(dic[a],1)
    print(ans)
if __name__ == '__main__':
    main()
