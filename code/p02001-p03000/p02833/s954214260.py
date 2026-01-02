#coding:utf-8
import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7


    def countZero(n):
        return len(str(n))-len(str(n).rstrip('0'))
    
    def f(n):
        if n < 2:
            return 1
        else:
            n2 = f(n-2)
            if n % 10 != 0 and countZero(n2) != countZero(n2*n):
                print(n,n2)
            return n * n2
    N = II()
    # fn = f(N)
    # print(fn)
    # print(countZero(fn))
    if N % 2 == 1:
        print(0)
        return
    else:
        ans = 0
        b = 10
        while (N-b)//b +1 > 0:
            ans += (N-b)//b +1
            b *= 5
        print(ans)
        # 10,20,30,40,50,100,110,200,1000,1010,1100,1200
        #50,150,250,950,1050,
        #250,750,1250
        #1250,2750
        return
if __name__ == '__main__':
    main()