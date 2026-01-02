#coding:utf-8
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = False
def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]

    N = II()
    P = input().replace(' ','')
    Q = input().replace(' ','')

    kouho = set(range(1,N+1))
    def kaijo(n):
        ans = 1
        for i in range(1,n+1):
            ans *= i
        return ans
    numbers = [0] * kaijo(N)
    # print(len(numbers))
    from copy import copy
    def mkp(kouho,i,p):
        if i == N-1:
            numbers.append(p+kouho[0])
            return

        for j in range(len(kouho)):
            kouho2 = copy(kouho)
            kouho2.remove(kouho[j])
            mkp(kouho2,i+1,p+kouho[j])
    mkp(list(map(str,range(1,N+1))),0,'')
    numbers = numbers[kaijo(N):]


    print(abs(numbers.index(P)-numbers.index(Q)))
    



   




if __name__ == '__main__':
    main()