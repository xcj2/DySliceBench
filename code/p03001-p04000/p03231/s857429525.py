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
    n,m = LI()
    s = S()
    t = S()
    l1 = lcm(n,m)
    s_unit = l1//n
    t_unit = l1//m
    l2 = lcm(s_unit, t_unit)
    time = (l1-1)//l2+1
    itr = [l2*i for i in range(time)]
    ans = l1

    for i in itr:
        si = i//s_unit
        ti = i//t_unit
        if s[si] != t[ti]:
            ans = -1

    print(ans)

main()            
