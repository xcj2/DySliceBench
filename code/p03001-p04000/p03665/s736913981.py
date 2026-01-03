import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    def select(n,k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    n,p = LI()
    a = LI()
    a = list(map(lambda x: x%2, a))
    dic = collections.Counter(a)
    c0 = dic[0]
    c1 = dic[1]
    ans = 0

    if p == 0:
        for i in range(n+1):
            for s in range(i//2+1):
                n1 = 2*s
                n0 = i-n1
                if n0<=c0 and n1<=c1:
                    ans += select(c0,n0)*select(c1,n1)
    else:
        for i in range(1,n+1):
            for s in range((i-1)//2+1):
                n1 = 2*s+1
                n0 = i-n1
                if n0<=c0 and n1<=c1:
                    ans += select(c0,n0)*select(c1,n1)
                    
    print(ans)

main()            
