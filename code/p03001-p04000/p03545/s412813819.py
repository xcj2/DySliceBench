import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    abcd = list(map(int,list(S())))
    bits = itertools.product([0,1],repeat=3)

    for bit in bits:
        cnt = abcd[0]
        for i,op in zip(abcd[1:],bit):
            if op == 0:
                cnt += i
            else:
                cnt -= i
        if cnt == 7:
            ans = str(abcd[0])
            for i,op in zip(abcd[1:],bit):
                ans += "+" if op == 0 else "-"
                ans += str(i)
            break
    ans += "=7"
    print(ans)
main()            
