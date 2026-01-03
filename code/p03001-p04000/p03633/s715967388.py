import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    from functools import reduce
    def lcm_base(n1,n2):
        return (n1*n2)//math.gcd(n1,n2)
    def lcm(*numbers):
        return reduce(lcm_base, numbers)

    n = I()
    t = [0 for _ in range(n)]
    for i in range(n):
        t[i] = I()

    ans = lcm(*t)
    print(ans)
main()            
