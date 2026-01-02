import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    from functools import reduce
    def lcm_base(n1,n2):
        return (n1*n2)//math.gcd(n1,n2)
    def lcm(*numbers):
        return reduce(lcm_base, numbers)
    a,b,c,d = LI()
    cd = lcm(c,d)
    lst = [c,d,cd]
    ans_lst = []
    for ex in lst:
        before = a if a % ex == 0 else a+ex-(a%ex)
        after = b - (b%ex)
        # print(ex,before,after)
        if before > after:
            ans_lst.append(0)
        else:
            bnum = before//ex
            anum = after//ex
            num = anum - bnum +1
            ans_lst.append(num)
            # print(anum,bnum,num)
    ans =(b-a +1) - (ans_lst[0] + ans_lst[1] - ans_lst[2])
    # print(ans_lst)
    print(ans)

main()